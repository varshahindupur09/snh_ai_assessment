# Tree API

## Setup

``` pip install -r requirements.txt ```
``` python -m uvicorn app.main:app --reload ```

## On Terminal
curl -X POST http://127.0.0.1:8000/api/tree \
     -H "Content-Type: application/json" \
     -d '{"label": "root"}'
O/P: {"parent_id":null,"id":1,"label":"root"}%  

curl -X POST http://127.0.0.1:8000/api/tree \
     -H "Content-Type: application/json" \
     -d '{"label": "bear", "parentId": 1}'
O/P:
{"parent_id":1,"id":2,"label":"bear"}%

curl -X POST http://127.0.0.1:8000/api/tree \
     -H "Content-Type: application/json" \
     -d '{"label": "cat", "parentId": 2}'

curl -X POST http://127.0.0.1:8000/api/tree \
     -H "Content-Type: application/json" \
     -d '{"label": "frog", "parentId": 1}'

curl -X POST http://127.0.0.1:8000/api/tree \
     -H "Content-Type: application/json" \
     -d '{"label": "cat’s child", "parentId": 3}'



## Response on terminal
curl -X GET http://127.0.0.1:8000/api/tree

{
  "id": 1,
  "label": "root",
  "children": [
    {
      "id": 2,
      "label": "bear",
      "children": [
        {
          "id": 3,
          "label": "cat",
          "children": [
            {
              "id": 5,
              "label": "cat’s child",
              "children": []
            }
          ]
        }
      ]
    },
    {
      "id": 4,
      "label": "frog",
      "children": []
    }
  ]
}