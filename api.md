# SpeechToText

Types:

```python
from andakia.types import SpeechToTextTranscribeResponse
```

Methods:

- <code title="post /asr">client.speech_to_text.<a href="./src/andakia/resources/speech_to_text.py">transcribe</a>(\*\*<a href="src/andakia/types/speech_to_text_transcribe_params.py">params</a>) -> <a href="./src/andakia/types/speech_to_text_transcribe_response.py">SpeechToTextTranscribeResponse</a></code>

# LanguageUnderstanding

Types:

```python
from andakia.types import LanguageUnderstandingTranslateResponse
```

Methods:

- <code title="post /comprehend">client.language_understanding.<a href="./src/andakia/resources/language_understanding.py">translate</a>(\*\*<a href="src/andakia/types/language_understanding_translate_params.py">params</a>) -> str</code>

# Authentication

Types:

```python
from andakia.types import AuthenticationLoginResponse
```

Methods:

- <code title="post /login">client.authentication.<a href="./src/andakia/resources/authentication.py">login</a>(\*\*<a href="src/andakia/types/authentication_login_params.py">params</a>) -> <a href="./src/andakia/types/authentication_login_response.py">AuthenticationLoginResponse</a></code>

# Purchases

Types:

```python
from andakia.types import Purchase, PurchaseCreateResponse, PurchaseListResponse
```

Methods:

- <code title="post /purchase">client.purchases.<a href="./src/andakia/resources/purchases.py">create</a>(\*\*<a href="src/andakia/types/purchase_create_params.py">params</a>) -> <a href="./src/andakia/types/purchase_create_response.py">PurchaseCreateResponse</a></code>
- <code title="get /purchase/{purchaseId}">client.purchases.<a href="./src/andakia/resources/purchases.py">retrieve</a>(purchase_id) -> <a href="./src/andakia/types/purchase.py">Purchase</a></code>
- <code title="get /purchase">client.purchases.<a href="./src/andakia/resources/purchases.py">list</a>() -> <a href="./src/andakia/types/purchase_list_response.py">PurchaseListResponse</a></code>

# Statistics

Types:

```python
from andakia.types import StatisticRetrieveResponse
```

Methods:

- <code title="get /statistic">client.statistics.<a href="./src/andakia/resources/statistics.py">retrieve</a>() -> <a href="./src/andakia/types/statistic_retrieve_response.py">StatisticRetrieveResponse</a></code>

# Tokens

Types:

```python
from andakia.types import (
    TokenCreateResponse,
    TokenRetrieveResponse,
    TokenListResponse,
    TokenDeleteResponse,
)
```

Methods:

- <code title="post /token">client.tokens.<a href="./src/andakia/resources/tokens.py">create</a>(\*\*<a href="src/andakia/types/token_create_params.py">params</a>) -> <a href="./src/andakia/types/token_create_response.py">TokenCreateResponse</a></code>
- <code title="get /token/{tokenName}">client.tokens.<a href="./src/andakia/resources/tokens.py">retrieve</a>(token_name) -> <a href="./src/andakia/types/token_retrieve_response.py">TokenRetrieveResponse</a></code>
- <code title="get /token">client.tokens.<a href="./src/andakia/resources/tokens.py">list</a>() -> <a href="./src/andakia/types/token_list_response.py">TokenListResponse</a></code>
- <code title="delete /token/{tokenName}">client.tokens.<a href="./src/andakia/resources/tokens.py">delete</a>(token_name) -> str</code>

# TextToSpeech

Methods:

- <code title="post /tts">client.text_to_speech.<a href="./src/andakia/resources/text_to_speech.py">create</a>(\*\*<a href="src/andakia/types/text_to_speech_create_params.py">params</a>) -> BinaryAPIResponse</code>

# Users

Types:

```python
from andakia.types import UserCreateResponse, UserRetrieveResponse, UserChangePasswordResponse
```

Methods:

- <code title="post /user">client.users.<a href="./src/andakia/resources/users.py">create</a>(\*\*<a href="src/andakia/types/user_create_params.py">params</a>) -> <a href="./src/andakia/types/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /user/{userId}">client.users.<a href="./src/andakia/resources/users.py">retrieve</a>(user_id) -> <a href="./src/andakia/types/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="post /user/change-password">client.users.<a href="./src/andakia/resources/users.py">change_password</a>(\*\*<a href="src/andakia/types/user_change_password_params.py">params</a>) -> str</code>
