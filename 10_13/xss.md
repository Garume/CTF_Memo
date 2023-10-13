---
marp: true
theme: gaia
style: div.mermaid { all: unset; }
---

# セキュリティコンテスト CTF で学ぶ脆弱性攻略の技術

8 章 XSS Cross-Site Scripting

チーム a 渡辺康介

---

## 目次

1. XSS とは
2. 簡単な例
3. 反射型 XSS
4. 蓄積型 XSS
5. Dom-base XSS
6. SCP
7. 実践

---

## XSS

XSS (Cross-Site Scripting)

-   Web の脆弱性の一つ
-   悪意のあるスクリプトが Web ページに挿入され、ユーザーのブラウザ上で実行される
-   主なタイプ:
    -   Reflected XSS (反射型 XSS)
    -   Stored XSS (蓄積型 XSS)
    -   DOM-based XSS

---

## 簡単な例

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
  name = request.args.get('name', 'unknown')
  return f'<p>Hello, {name}!</p>'

app.run(host='0.0.0.0', port=5000)
```

起動したのちに接続すると、
`<p>Hello, unknown!</p>`

---

## 簡単な例

ここで任意の JavaScript コードを実行したい。
例えば、次のようなクエリを含めてリクエストを送信すると、図 8-1 のようにアラートできる。
`localhost:5000?name=</p><script>alert()</script><p>`

---

## XSS の種類の説明

-   Reflected XSS (反射型 XSS)
-   Stored XSS (蓄積型 XSS)
-   DOM-based XSS

p.134 ~ p.140

---

## 反射型 XSS

-   ユーザーがクリックしたリンクや入力したデータを通じて、悪意のあるスクリプトが Web ページに反映される形式の XSS。
-   この攻撃は、ユーザーが特定のリンクをクリックすることで発生。
-   攻撃者は、悪意のあるリンクをメールや SNS などでユーザーに送り、クリックさせることで攻撃を実行します。

---

## 反射型 XSS

<div class="mermaid">
sequenceDiagram
    participant Attacker as 攻撃者
    participant Victim as 被害者
    participant Browser as ブラウザ
    participant Server as サーバ
    Attacker->>Victim: 悪意のあるリンクを送る
    Victim->>Browser: 悪意のあるリンクをクリック
    Browser->>Server: リクエストを送信
    Server->>Browser: 悪意のあるスクリプトを含むレスポンス
    Browser->>Victim: スクリプト実行
</div>

<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.0/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });
window.addEventListener('vscode.markdown.updateContent', function() { mermaid.init() });
</script>

---

## 蓄積型 XSS

-   悪意のあるスクリプトが Web サーバー上に保存され、その後、他のユーザーがそのページを閲覧することでスクリプトが実行される形式の XSS。
-   例えば、掲示板やコメント欄など、ユーザーが情報を投稿できる場所で発生することが多い。

---

## 反射型 XSS

<div class="mermaid">
sequenceDiagram
    participant Attacker as 攻撃者
    participant Victim as 被害者
    participant Browser as ブラウザ
    Attacker->>Victim: 悪意のあるページを送る
    Victim->>Browser: 悪意のあるページを開く
    Browser->>Browser: DOMを操作してスクリプト実行
</div>

<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.0/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });
window.addEventListener('vscode.markdown.updateContent', function() { mermaid.init() });
</script>

---

## Dom-base XSS

-   Web ページの DOM（Document Object Model）を操作して発生する XSS です。
-   JavaScript がクライアントサイドで DOM を動的に変更する際に、悪意のあるスクリプトが実行されることで攻撃が成立します。

---

## Dom-base XSS

<div class="mermaid">
sequenceDiagram
    participant Attacker as 攻撃者
    participant Victim as 被害者
    participant Browser as ブラウザ
    participant Server as サーバ
    Attacker->>Victim: 悪意のあるデータを送る
    Victim->>Browser: 悪意のあるデータを入力
    Browser->>Server: データを保存
    Server->>Browser: 保存されたデータを含むレスポンス
    Browser->>Victim: スクリプト実行
</div>

<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.0/dist/mermaid.esm.min.mjs';
mermaid.initialize({ startOnLoad: true });
window.addEventListener('vscode.markdown.updateContent', function() { mermaid.init() });
</script>

---

## CSP (Content Security Policy)

-   XSS 攻撃を防ぐためのセキュリティポリシー
-   Web ページがどの外部リソースを読み込むことができるかを制限する
-   例: Content-Security-Policy: Script-src 'self' は、現在のドメインからのスクリプトのみを許可する

---

## ディレクティブ

-   CSP による制限を定義する。

本書で説明されているディレクティブ

-   script-src
-   connect-src
-   default-src
-   base-uri

---

## 実践

本書を利用して、環境を構築してもよいが、今回は Google が作った`XSS Games`というサイトでやってみることにする。

https://xss-game.appspot.com

スライドは以上。
