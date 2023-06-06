import pytest
from rest_framework.test import APIClient
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.reverse import reverse
from model_bakery import baker


from students.models import Student, Course

@pytest.fixture
def api_client():
    """Фикстура для APIClient"""
    return APIClient()

@pytest.fixture
def student_factory():
    """Фикстура фабрики студентов"""
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture
def course_factory():
    """Фикстура фабрики курсов"""
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_one_cource(api_client, course_factory):
    """Проверка получения первого курса"""
    courses = course_factory(_quantity=1)
    url = f"http://127.0.0.1:8000/api/v1/courses/{courses[0].id}/"
    responce = api_client.get(url)
    assert responce.status_code == HTTP_200_OK
    data = responce.json()
    assert courses[0].id == data['id']
    
@pytest.mark.django_db
def test_list_cource(api_client, course_factory):
    """Проверка получения списка курсов"""
    courses = course_factory(_quantity=10)
    url = "http://127.0.0.1:8000/api/v1/courses/"
    responce = api_client.get(url)
    assert responce.status_code == HTTP_200_OK
    data = responce.json()
    for i, course in enumerate(data):
        assert courses[i].id == course['id']

@pytest.mark.django_db
def test_filter_id(api_client, course_factory):
    """Проверка фильтрации курсов по ID"""
    courses = course_factory(_quantity=10)
    for cource in courses:
        url = f"http://127.0.0.1:8000/api/v1/courses/?id={cource.id}"
        responce = api_client.get(url)
        assert responce.status_code == HTTP_200_OK
        data = responce.json()
        assert cource.id == data[0]['id']

@pytest.mark.django_db
def test_filter_name(api_client, course_factory):
    """Проверка фильтрации курсов по name"""
    courses = course_factory(_quantity=10)
    for cource in courses:
        url = f"http://127.0.0.1:8000/api/v1/courses/?name={cource.name}"
        responce = api_client.get(url)
        assert responce.status_code == HTTP_200_OK
        data = responce.json()
        assert cource.name == data[0]['name']

@pytest.mark.django_db
def test_create_cource(api_client):
    """Проверка создания курса через POST запрос"""
    url = "http://127.0.0.1:8000/api/v1/courses/"
    data = {
        'name': 'Физика'
    }
    responce = api_client.post(url, data)
    assert responce.status_code == HTTP_201_CREATED

@pytest.mark.django_db
def test_update_cource(api_client, course_factory):
    """Проверка изменения курса"""
    courses = course_factory(_quantity=1)
    url = f"http://127.0.0.1:8000/api/v1/courses/{courses[0].id}/"
    data = {
        'name': 'Психология'
    }
    responce = api_client.patch(url, data)
    assert responce.status_code == HTTP_200_OK
    responce = api_client.put(url, data)
    assert responce.status_code == HTTP_200_OK
    
@pytest.mark.django_db
def test_delete_cource(api_client, course_factory):
    """Проверка удаления курса"""
    courses = course_factory(_quantity=1)
    url = f"http://127.0.0.1:8000/api/v1/courses/{courses[0].id}/"
    responce = api_client.delete(url)
    assert responce.status_code == HTTP_204_NO_CONTENT