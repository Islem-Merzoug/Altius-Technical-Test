import json

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestServices:
    def test_one_exercice_one(self):
        """Test exercice_one with assignment01-1 sample data."""
        with open('materials/Inputs/assignment01-1.txt') as f:
            lines = f.read().splitlines()
            lines = [int(i) for i in lines]

        response = client.post(
            "/exercice-one",
            data=json.dumps(
                lines
            )
        )

        assert response.status_code == 200
        json_response = response.json()
        assert json_response == [0, 1]

    def test_two_exercice_one(self):
        """Test exercice_one with assignment01-2 sample data."""
        with open('materials/Inputs/assignment01-2.txt') as f:
            lines = f.read().splitlines()
            lines = [int(i) for i in lines]
        print('haha:', lines)

        response = client.post(
            "/exercice-one",
            data=json.dumps(
                lines
            )
        )

        assert response.status_code == 200
        json_response = response.json()
        assert json_response == [1, 0]



    def test_one_exercice_two(self):
        """Test exercice_two with assignment02-1 sample data."""
        with open('materials/Inputs/assignment02-1.txt') as f:
            l = f.read().splitlines()
            lines = l[1].split(" ")
            lines.insert(0, l[0])

        print('haha:', lines)

        response = client.post(
            "/assignement-two",
            data=json.dumps(
                lines
            )

        )

        assert response.status_code == 200
        json_response = response.json()
        assert json_response == 3


    def test_two_exercice_two(self):
        """Test exercice_two with assignment02-2 sample data."""
        with open('materials/Inputs/assignment02-2.txt') as f:
            l = f.read().splitlines()
            lines = l[1].split(" ")
            lines.insert(0, l[0])

        print('haha:', lines)

        response = client.post(
            "/assignement-two",
            data=json.dumps(
                lines
            )

        )

        assert response.status_code == 200
        json_response = response.json()
        assert json_response is None
