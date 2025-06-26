# UMS API - University Management System API

A comprehensive FastAPI-based REST API for University Management System with features including user management, timetable management, announcements, hostel management, and placement portal.

## 🚀 Features

- **User Management** - Student and faculty authentication and profile management
- **Timetable Management** - Course scheduling and timetable generation
- **Announcements** - University-wide announcements and notifications
- **Hostel Management** - Student accommodation and room allocation
- **Placement Portal** - Job postings and placement opportunities
- **Miscellaneous Services** - Additional utility endpoints

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.11
- **Deployment**: Vercel (Serverless)
- **Documentation**: Auto-generated Swagger UI
- **Testing**: Pytest

## 📋 Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Git

## 🚀 Installation & Setup

### Method 1: Local Development

```bash
# Clone the repository
git clone https://github.com/Krixhnnna/UMS_API

# Navigate to the project directory
cd UMS_API

# Install virtualenv (if not already installed)
pip install virtualenv

# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Rename .env.example to .env and fill in the required details
cp .env.example .env

# Start the development server
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Access the API documentation
# Open http://localhost:8000/docs in your browser
```

### Method 2: Using Docker

```bash
# Clone the repository
git clone https://github.com/Krixhnnna/UMS_API

# Navigate to the project directory
cd UMS_API

# Build the Docker image
docker-compose build

# Set up environment variables for Docker
# Rename .env.example to .env.docker and fill in the required details
cp .env.example .env.docker

# Start the application using Docker Compose
docker-compose --env-file ./.env.docker up

# Access the API documentation
# Open http://localhost:8000/docs in your browser
```

## 🧪 Testing

```bash
# Run test cases
pytest tests/test.py

# Run all tests with coverage
pytest --cov=app tests/
```

## 📚 API Documentation

Once the server is running, you can access:

- **Interactive API Documentation**: `http://localhost:8000/docs`
- **Alternative Documentation**: `http://localhost:8000/redoc`
- **Health Check**: `http://localhost:8000/health`

## 🌐 Production Deployment

This API is deployed on Vercel and accessible at:
**https://ums-au3q0at17-krishnas-projects-e779cec0.vercel.app**

### Production Endpoints:
- **Health Check**: `/health`
- **API Documentation**: `/docs`
- **User Management**: `/api/v1/user/...`
- **Timetable**: `/api/v1/timetable/...`
- **Announcements**: `/api/v1/announcement/...`
- **Miscellaneous**: `/api/v1/misc/...`
- **Hostel Management**: `/api/v1/hostel/...`
- **Placement Portal**: `/api/v1/placement/...`

## 📁 Project Structure

```
UMS_API/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── Config.py            # Configuration settings
│   ├── routers/             # API route definitions
│   ├── schema/              # Pydantic models
│   ├── services.py          # Business logic
│   ├── utilities/           # Utility functions
│   └── scrapers/            # Web scraping modules
├── tests/                   # Test files
├── assets/                  # Static assets
├── requirements.txt         # Python dependencies
├── docker-compose.yml       # Docker configuration
├── Dockerfile              # Docker image definition
├── vercel.json             # Vercel deployment configuration
└── README.md               # This file
```

## 🔧 Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
APP_NAME=UMS API
APP_VERSION=1.0.0
APP_DESCRIPTION=University Management System API
PYTHON_ENV=development
DOCS_ENABLED=true
LPU_LIVE_TOKEN=your_token_here
REG_NO=your_registration_number
PASSWORD=your_password
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Krishna**
- GitHub: [@Krixhnnna](https://github.com/Krixhnnna)
- Email: krishna@example.com

## 🙏 Acknowledgments

- FastAPI community for the excellent framework
- Vercel for seamless deployment
- All contributors who helped improve this project

## 📞 Support

If you encounter any issues or have questions, please:

1. Check the [API Documentation](https://ums-au3q0at17-krishnas-projects-e779cec0.vercel.app/docs)
2. Open an issue on GitHub
3. Contact the maintainer

---

**Made with ❤️ by Krishna** 