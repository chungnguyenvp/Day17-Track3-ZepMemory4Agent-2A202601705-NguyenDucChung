# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **938.1 ms**
- Average token reduction vs full source context: **14.2%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | PASS | 899.1 | 148 | 67.8% |  |
| E09 | long_term | PASS | 1532.8 | 857 | 0.0% |  |
| E10 | short_term | PASS | 0.2 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1384.9 | 1428 | 0.0% |  |
| E03 | long_term | PASS | 2007.7 | 1452 | 0.0% |  |
| E04 | episodic | PASS | 266.6 | 596 | 0.0% |  |
| E05 | episodic | PASS | 302.9 | 586 | 0.0% |  |
| E07 | mixed | PASS | 2061.6 | 485 | 14.2% |  |
| E11 | semantic | PASS | 250.0 | 146 | 74.2% |  |
| E08 | long_term | PASS | 1613.4 | 1458 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata=`

### E09 - long_term

`<USER_SUMMARY> Lan Tran's project is LOTUS-88, for which they prioritize Java and Spring Boot for backend development examples.  The user prioritizes Java and Spring Boot for backend development and explicitly avoids using Python for backend tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 04:38:46     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan uu tien stack backend nao cho LOTUS-88?   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Ja`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh prefers Python a`

### E03 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh prefers Python a`

### E04 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Minh con open loop hay deadline nao chua hoan thanh? EPISODE: Minh dang lam kiem ke lai mo hinh cac du an backend de bao cao, ma minh rat so cai vu bi gan nham du an cua nguoi khac vao ho so cua minh, chuyen do tung xay ra roi nen lan nay min EPISODE: Minh dang setup lai moi truong dev cho mot buoi ngoi code mot minh cuoi tuan nay, kieu khong co ai chung nhom, chi lam project rieng cua min`

### E05 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Minh dang lam kiem ke lai mo hinh cac du an backend de bao cao, ma minh rat so cai vu bi gan nham du an cua nguoi khac vao ho so cua minh, chuyen do tung xay ra roi nen lan nay min EPISODE: Minh dang setup lai moi truong dev cho mot buoi ngoi code mot minh cuoi tuan nay, kieu khong co ai chung nhom, chi lam project rieng cua minh cho vui thoi. Truoc khi minh chon temp EPISODE: Sang mai min`

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh pref`

### E11 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata=`

### E08 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27, for which Python is preferred. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh needs to complete a benchmark report, which is an open-loop LAB-REPORT-1600, before Friday at 16:00. Minh is currently debugging async HTTP requests and has encountered failures despite increasing the timeout to 60s. Minh believes the main issue is connection churn, not timeout thresholds, and has identified the problem as related to ASYNC-FIX-20. Minh suggested reusing an aiohttp ClientSession and setting concurrency to 20 as an effective solution.  Minh prefers Python a`
