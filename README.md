# nft_backend

**Backend for the NFT project/game.**  

<img src="https://img.shields.io/badge/Django-5.2-green" alt="Django"> <img src="https://img.shields.io/badge/Python-3.13+-blue" alt="Python"> <img src="https://img.shields.io/badge/PostgreSQL-14+-blue" alt="PostgreSQL">


##  Technology Stack
| Component       | Technology |
|-----------------|------------|
| Backend         | Django 5.2 |
| Database        | PostgreSQL |
| Admin Interface | Django Admin (customized) |

##  Quick start(with Docker)


### Installation
```bash
# 1. Clone repository
git clone https://github.com/t1matoma/nft_backend.git
cd nft_backend

```
### Build and start containers

```bash
docker-compose up --build -d
```
#### Run migrations inside the django container

```bash
docker-compose exec django python manage.py makemigrations
docker-compose exec django python manage.py migrate
```

#### Create a superuser
```bash
docker-compose exec django python manage.py createsuperuser
```

#### The app will be available at:
`http://localhost:8000/`

## How to use(in postman)

### For create new users
`http://localhost:8000/users/`

```bash
{
    "username": "your user name",
    "email": "your email"
}
```

### For create new QR code
`http://localhost:8000/qr/generate/`


response, not request:
```bash
{
    "id": 1,
    "code": "code",
    "created_at": "date"
}
```

use code for scan QR code

### For scan QR code
`http://localhost:8000/nft/scan/`
```bash
{
    "user_id": 1,
    "qr_code": "code"
}
```
