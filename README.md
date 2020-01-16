# Python GUI Examples

### 1. Tkinter & MySql (Wishlist Example)

#### Python Verssion
```shell
> python --version
Python 3.8.1
```

#### Python Virtual Environments. Venv installation on Windows

```shell
> python -m venv venv
```

#### Activate and Deactivate venv

```shell
cd c:/puthon_gui
venv\Scripts\activae
venv\scripts\deactivate
```

* Note: Use <**Scripts**> with <**S**> or <**scripts**> with <**s**>

#### PIP LIST

```shell
pip list
```

#### PIP UPGRADE

```shell
python -m pip install --upgrade pip
```

#### PIP for this example (Tkinter & MySQL)

```shell
pip install pymysql
pip install Pillow
pip install pyinstaller
```

#### PIP FREEZE

```shell
pip freeze > requirements.txt
```

#### Requirements. requirements.txt

```markdown
altgraph==0.17
future==0.18.2
pefile==2019.4.18
Pillow==7.0.0
PyInstaller==3.6
PyMySQL==0.9.3
pywin32-ctypes==0.2.0
```

#### PIP INSTALL REQUIREMENTS

```shell
pip -r install requirements.txt
```

#### MySQL

* In order to connect with your own database, replace the following credential in the file `wishlist.py` line `№. 27`: 

  ```python
  conn = pymysql.connect(host = '<Host>', user = '<User>', password = '<Password>', db = '<Database Name>')
  ```

   [![Clever Cloud](logo_on_white-1579091213548.svg)](https://console.clever-cloud.com/) 

* Go to Clever Cloud and create account in order to connect with MySQL 

  `Clever Cloud` -> `Your Account` -> `Create` -> `Select MySQL`  -> `Price with 0.00 € (Free Plan)` -> `MySQL add-on (name)` -> `Database Credentials`.

* Go to `PHPMyAdmin` and create Wishlist table as following:

  ```sql
  --
  -- Table structure for table `wishlist`
  --
  
  CREATE TABLE `wishlist` (
    `prod_id` int(11) NOT NULL,
    `title` text NOT NULL,
    `price` text NOT NULL,
    `status` text NOT NULL,
    `link` text NOT NULL,
    `note` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `contact` text NOT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
  
  --
  -- Indexes for dumped tables
  --
  
  --
  -- Indexes for table `wishlist`
  --
  ALTER TABLE `wishlist`
    ADD PRIMARY KEY (`prod_id`);
  
  --
  -- AUTO_INCREMENT for dumped tables
  --
  
  --
  -- AUTO_INCREMENT for table `wishlist`
  --
  ALTER TABLE `wishlist`
    MODIFY `prod_id` int(11) NOT NULL AUTO_INCREMENT;
  COMMIT;
  ```

#### Run Script

```shell
> python wishlist.py
```

#### Installation for Windows (wishlist.exe) and Mac OS

To create wishlist.exe all you need to do is call `pyinstaller` and then point to your script. So, in this case, our main script is`wishlist.py`.

```
pyinstaller --onefile --windowed wishlist.py
```

Go to the dist folder you will get wishlist.exe (windows OS).