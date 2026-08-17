# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1290.5 ms**
- Average token reduction vs full source context: **6.3%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G08 | long_term | PASS | 3197.1 | 870 | 0.0% |  |
| G09 | long_term | PASS | 1677.6 | 1476 | 0.0% |  |
| G12 | semantic | PASS | 653.9 | 418 | 8.9% |  |
| G14 | semantic | PASS | 259.3 | 270 | 30.2% |  |
| G15 | semantic | PASS | 268.7 | 270 | 41.2% |  |
| G19 | mixed | PASS | 2711.8 | 581 | 0.0% |  |
| G03 | long_term | PASS | 1948.0 | 1471 | 0.0% |  |
| G04 | long_term | PASS | 1701.2 | 1447 | 0.0% |  |
| G05 | long_term | PASS | 1503.7 | 1450 | 0.0% |  |
| G10 | episodic | PASS | 254.9 | 470 | 0.0% |  |
| G11 | episodic | PASS | 262.3 | 468 | 0.0% |  |
| G13 | semantic | PASS | 275.7 | 416 | 26.4% |  |
| G16 | mixed | PASS | 2308.7 | 581 | 0.0% |  |
| G18 | mixed | PASS | 844.9 | 500 | 11.5% |  |
| G20 | mixed | PASS | 2650.5 | 831 | 0.0% |  |
| G06 | long_term | PASS | 1493.9 | 1469 | 0.0% |  |
| G07 | long_term | PASS | 1452.7 | 1452 | 0.0% |  |
| G17 | mixed | PASS | 2345.2 | 581 | 8.1% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G08 - long_term

`<USER_SUMMARY> Lan Tran's project is LOTUS-88, for which they prioritize Java and Spring Boot for backend development examples.  The user prioritizes Java and Spring Boot for backend development and explicitly avoids using Python for backend tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: messag`

### G09 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh prefers Python a`

### G12 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal `

### G14 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G15 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan Tran's project is LOTUS-88, for which they prioritize Java and Spring Boot for backend development examples.  The user prioritizes Java and Spring Boot for backend development and explicitly avoids using Python for backend tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 04:38:46     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan uu tien stack backend nao cho LOTUS-88?   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: `

### G03 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh prefers Python a`

### G04 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh prefers Python a`

### G05 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh prefers Python a`

### G10 - episodic

`EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Minh con open loop hay deadline nao `

### G11 - episodic

`EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Minh con open loop hay deadline nao `

### G13 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data witho`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh pref`

### G18 - mixed

`<EPISODIC> EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Voi demo ca nhan cua Minh, ngon ngu uu tien la gi? EPISODE: Minh dang lam kiem ke lai mo hinh cac du an backend de bao cao, ma minh rat so cai vu bi ga`

### G20 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh pref`

### G06 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh prefers Python a`

### G07 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh prefers Python a`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh pref`
