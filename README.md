# python-junior-backend

Hi,

此專案為 Tradingvalley 的 junior 後端工程師的試前作業，請 fork 此專案，以 python 撰寫每道問題。

完成後，請 PR 此專案。

### 題目一：以 Flask 實作一個簡易的會員系統

功能需求：

1. 實作三隻 API （註冊、登入、獲取會員資料）
    * [POST] 註冊
    * [POST] 登入（如登入成功獲取 token）
    * [GET] 獲取會員資料 （以 token 取得會員資料）
2. 以 ORM 框架 SQLAlchemy 實作 MySQL
3. 資料庫內容及格式可自行設計，但必須包含以下資訊
    * username
    * password
    * name
    * email
4. 撰寫 OpenAPI Spec (yaml format)


---------
### 題目二：裝飾器的使用

功能需求：

衍伸第一題，在登入的 API 中，實作一個裝飾器，每當是第一次登入時都會 print "Welcome back {name}".

---------

### 交付項目：

*  請以 python 3.10+ 撰寫，可自由選用擅長的套件
*  若覺得需要，可以自由選用各類外部服務，如 cache
*  請以 docker 建置及安裝各類外部服務
