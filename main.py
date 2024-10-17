from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
import geopandas as gpd
from shapely.geometry import Point
import os
from rtree import index
from typing import Dict, Any

# Initialize FastAPI app
app = FastAPI(
    title="Geospatial Lookup Service",
    description="A service to lookup region information based on latitude and longitude coordinates",
    version="1.0.0"
)

# Read the shapefile
shapefile_path = "shapefile/"
gdf = gpd.read_file(shapefile_path)

# Create a spatial index
idx = index.Index()
for id, geometry in enumerate(gdf.geometry):
    idx.insert(id, geometry.bounds)


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """
    Health check endpoint to verify service status
    """
    return {"status": "healthy"}


@app.get("/")
async def health_check_root() -> Dict[str, str]:
    """
    Root endpoint health check
    """
    return {"status": "healthy"}


@app.get("/lookupezone")
async def get_shape_attributes(
        lat: float = Query(..., description="Latitude of the point to lookup"),
        lon: float = Query(..., description="Longitude of the point to lookup")
) -> Dict[str, Any]:
    """
    Lookup region information based on latitude and longitude coordinates

    Args:
        lat (float): Latitude of the point
        lon (float): Longitude of the point

    Returns:
        Dict containing region information or error message

    Raises:
        HTTPException: If point is not found in any region or if an error occurs
    """
    try:
        # Create a Shapely Point object from the latitude and longitude
        point = Point(lon, lat)
        point = gpd.GeoSeries(point, crs="EPSG:4326").to_crs(gdf.crs).iloc[0]

        # Use spatial index for initial filtering
        possible_matches_idx = list(idx.intersection(point.bounds))
        possible_matches = gdf.iloc[possible_matches_idx]

        for _, row in possible_matches.iterrows():
            if point.within(row.geometry):
                # If the point is contained within the current feature, return the attributes
                attributes = row.drop('geometry').to_dict()
                return {"Region": attributes}

        # If no containing shape is found, raise 404 exception
        raise HTTPException(
            status_code=404,
            detail="Point not within any shape in the shapefile."
        )

    except Exception as e:
        # Log the error and raise 500 exception
        print(f"An error occurred: {str(e)}")  # Replace with proper logging
        raise HTTPException(
            status_code=500,
            detail="An internal server error occurred."
        )


# Configure host and port using environment variables
host = os.getenv('HOST', '0.0.0.0')
port = int(os.getenv('PORT', 80))

# Run the FastAPI app using uvicorn server
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host=host, port=port)
