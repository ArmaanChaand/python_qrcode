
# Python Flask QR Code generator 

A minimal QR Code image generator for texts prompted.



## Live Preview 

[https://pyqrcode.vercel.app](https://pyqrcode.vercel.app/)


## API Reference

#### Get QR image

```http
  GET /generate_qr_code
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `text` | `string` | **Required**. Text to be encoded in QR |




## Run Locally

Clone the project

```bash
  git clone https://github.com/ArmaanChaand/python_qrcode.git
```

Go to the project directory

```bash
  cd python_qrcode
```

Install dependencies

```bash
  python -m pip install -r requirements.txt
```

Start the server

```bash
  python main.py
```


## Authors

- [@ArmaanChaand](https://www.github.com/ArmaanChaand)


## Contributing

Contributions are welcome! If you would like to contribute to this project, please open an issue or submit a pull request.

