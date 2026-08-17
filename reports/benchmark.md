# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **815.8 ms**
- Average token reduction vs full source context: **14.2%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | PASS | 553.2 | 148 | 67.8% |  |
| E09 | long_term | PASS | 1459.6 | 842 | 0.0% |  |
| E10 | short_term | PASS | 0.2 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1376.7 | 1490 | 0.0% |  |
| E03 | long_term | PASS | 1403.2 | 1495 | 0.0% |  |
| E04 | episodic | PASS | 555.7 | 332 | 0.0% |  |
| E05 | episodic | PASS | 258.9 | 351 | 0.0% |  |
| E07 | mixed | PASS | 1686.4 | 485 | 14.2% |  |
| E11 | semantic | PASS | 259.3 | 146 | 74.2% |  |
| E08 | long_term | PASS | 1420.1 | 1493 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata=`

### E09 - long_term

`<USER_SUMMARY> Lan Tran's project is LOTUS-88, for which they prioritize Java and Spring Boot for backend development examples.  The user prioritizes Java and Spring Boot for backend development and explicitly avoids using Python for backend tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-17 04:12:39     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan u`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> The user is learning about async/await and coroutines versus Tasks. They are debugging async HTTP requests and have identified that connection churn is the main issue, not the timeout threshold. Reusing an aiohttp ClientSession and setting concurrency to 20 has proven effective in resolving this. The user has a personal project named ORCHID-27 and a task to complete a benchmark report by Saturday at 16:00, associated with open loop LAB-REPORT-1600. For company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. Python is still preferred for personal demos like ORCHID-27.  The user prefers Python and dislikes Java. They are currently learning about asy`

### E03 - long_term

`<USER_SUMMARY> The user is learning about async/await and coroutines versus Tasks. They are debugging async HTTP requests and have identified that connection churn is the main issue, not the timeout threshold. Reusing an aiohttp ClientSession and setting concurrency to 20 has proven effective in resolving this. The user has a personal project named ORCHID-27 and a task to complete a benchmark report by Saturday at 16:00, associated with open loop LAB-REPORT-1600. For company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. Python is still preferred for personal demos like ORCHID-27.  The user prefers Python and dislikes Java. They are currently learning about asy`

### E04 - episodic

`EPISODE: Voi demo ca nhan cua Minh va du an BLUEBIRD-42, ngon ngu va stack backend uu tien hien tai la gi? Hay tra loi chi tiet, neu ro bang chung tu memory, giai thich vi sao chon layer do EPISODE: Backend cua BLUEBIRD-42 bat buoc dung stack gi? EPISODE: Voi demo ca nhan cua Minh, ngon ngu uu tien la gi? EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP.`

### E05 - episodic

`EPISODE: Voi demo ca nhan cua Minh va du an BLUEBIRD-42, ngon ngu va stack backend uu tien hien tai la gi? Hay tra loi chi tiet, neu ro bang chung tu memory, giai thich vi sao chon layer do EPISODE: Backend cua BLUEBIRD-42 bat buoc dung stack gi? EPISODE: Voi demo ca nhan cua Minh, ngon ngu uu tien la gi? EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP.`

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> The user is learning about async/await and coroutines versus Tasks. They are debugging async HTTP requests and have identified that connection churn is the main issue, not the timeout threshold. Reusing an aiohttp ClientSession and setting concurrency to 20 has proven effective in resolving this. The user has a personal project named ORCHID-27 and a task to complete a benchmark report by Saturday at 16:00, associated with open loop LAB-REPORT-1600. For company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. Python is still preferred for personal demos like ORCHID-27.  The user prefers Python and dislikes Java. They are currently learni`

### E11 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata=`

### E08 - long_term

`<USER_SUMMARY> The user is learning about async/await and coroutines versus Tasks. They are debugging async HTTP requests and have identified that connection churn is the main issue, not the timeout threshold. Reusing an aiohttp ClientSession and setting concurrency to 20 has proven effective in resolving this. The user has a personal project named ORCHID-27 and a task to complete a benchmark report by Saturday at 16:00, associated with open loop LAB-REPORT-1600. For company project BLUEBIRD-42, the backend must use TypeScript with NestJS, not Python. Python is still preferred for personal demos like ORCHID-27.  The user prefers Python and dislikes Java. They are currently learning about asy`
