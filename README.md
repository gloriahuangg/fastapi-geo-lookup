
# 🌍 FastAPI Geospatial Lookup Service

A high-performance REST API service for geospatial region lookups using shapefiles. Quickly determine which region a point falls within based on latitude and longitude coordinates.

<p align="center">
  <img src="/api/placeholder/800/400" alt="Geospatial Lookup Service Architecture" width="800"/>
</p>

## ✨ Features

- 🚀 Fast spatial lookups using R-tree indexing
- 📁 Support for custom shapefiles
- 🔍 RESTful API endpoints
- 📚 Auto-generated API documentation (Swagger/ReDoc)
- ❤️ Health check endpoints
- 🐳 Docker support
- ⚙️ Environment variable configuration

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Shapefile data
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/fastapi-geo-lookup.git
cd fastapi-geo-lookup
```

2. **Set up virtual environment**
```bash
python -m venv venv
# For Unix/macOS:
source venv/bin/activate
# For Windows:
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Add your shapefile**
- Place your shapefile data in the `shapefile/` directory

5. **Run the application**
```bash
uvicorn main:app --host 0.0.0.0 --port 80 --reload
```

Visit `http://localhost:80/docs` for interactive API documentation.

## 🔧 Configuration

Configure using environment variables:

```env
HOST=0.0.0.0    # Default host
PORT=80         # Default port
```

## 🐳 Docker Support

```bash
# Build the image
docker build -t geo-lookup-service .

# Run the container
docker run -p 80:80 -v /path/to/your/shapefile:/app/shapefile geo-lookup-service
```

## 📚 API Documentation

### Health Check

```http
GET /health
GET /
```

Response:
```json
{
    "status": "healthy"
}
```

### Geospatial Lookup

```http
GET /lookup?lat={latitude}&lon={longitude}
```

Example:
```bash
curl "http://localhost:80/lookupezone?lat=37.7749&lon=-122.4194"
```

Successful Response:
```json
{
    "Region": {
        "name": "San Francisco",
        "state": "California",
        "country": "USA"
    }
}
```

## ⚡ Performance

- R-tree spatial indexing for efficient queries
- In-memory shapefile data
- Async endpoint handlers
- Optimized spatial filtering

## 🛠️ Development Setup

1. **Install development dependencies**
```bash
pip install -r requirements-dev.txt
```

2. **Run tests**
```bash
pytest
```

3. **Format code**
```bash
black .
```

4. **Run linting**
```bash
flake8
```

## 📦 Project Structure

```
fastapi-geo-lookup/
├── main.py              # Main application file
├── requirements.txt     # Production dependencies
├── requirements-dev.txt # Development dependencies
├── Dockerfile          # Docker configuration
├── .gitignore         
├── tests/              # Test directory
└── shapefile/          # Directory for shapefile data
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [GeoPandas](https://geopandas.org/) - For geospatial operations
- [Rtree](https://rtree.readthedocs.io/) - For spatial indexing

## 📫 Support

- Create an issue in this repository
- Submit a pull request
- Contact the maintainers

## 🔮 Future Improvements

- [ ] Add support for multiple shapefile formats
- [ ] Implement caching layer
- [ ] Add batch processing endpoint
- [ ] Create CI/CD pipeline
- [ ] Add more detailed logging
- [ ] Implement rate limiting

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/yourusername">GloriaHuang</a>
</p>


