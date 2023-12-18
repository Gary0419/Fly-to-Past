# Airline
以下使用VS Code進行示範。

## 1. 安裝資料庫備份檔
在PostgreSQL安裝根目錄底下的airline.sql，請注意若PostgreSQL的版本過舊，可能會出現安裝失敗的情形。

## 2. 修改.env
打開根目錄底下的.env並填寫連線到資料庫的相關資訊，若相關設定有所不同，請依照註解中的格式進行修改。

![image](https://hackmd.io/_uploads/ByArYMR8p.png)

## 3. 進入虛擬環境並安裝所需套件

1. 開啟終端機，並移動路徑到專案根目錄
2. 輸入以下指令進入虛擬環境
```
db_env\Scripts\activate
```
3. 輸入以下指令安裝所需套件
```
pip install -r requirements.txt
```
4. 輸入以下指令啟動flask
```
flask run
```
