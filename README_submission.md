# Lab 17 — Multi-Memory Agent với Zep

**11/11 PASS (100%)**; no-memory 2/11 (18.2%). Nguồn: `reports/benchmark.json`.

## 1. Layer quan trọng nhất

Long-term: quyết định E02, E03, E08, E09 (20đ) và một nửa E07. Layer duy nhất chứng minh cross-session recall — E02 lấy preference từ session cũ trên thread mới, E09 kiểm tra user isolation. Semantic phủ E06/E11 nhưng chỉ là kho tĩnh dùng chung.

## 2. Trade-off Zep vs Redis + Qdrant

Redis + Qdrant cho quyền kiểm soát: TTL, schema, dữ liệu tại chỗ, độ trễ gần 0; đổi lại phải tự trích xuất fact và xử lý xung đột — Redis không tự hiểu "TypeScript đã thay Python". Zep làm sẵn: fact graph có `valid_at`/`invalid_at` và Context Block theo relevance. Giá: 1634.7ms mỗi truy vấn long-term (local 0.1ms), ingestion bất đồng bộ, dữ liệu ở bên thứ ba — lý do lab bắt buộc consent gate và drill xóa.

## 3. Guardrail chống memory poisoning

**Consent gate:** `require_memory_consent` chặn ingest nếu `consent.json` không opt-in; `minimize_pii` redact email/phone. **Giới hạn tiến trình nền:** heartbeat chỉ được dedupe note, đánh dấu task cũ, tạo recap — cấm tự thêm instruction hay quyền vào durable memory, nên câu chèn vào hội thoại không tự nâng thành luật. **Provenance:** fact nào cũng có nguồn và khoảng hiệu lực nên fact bẩn truy ngược, vô hiệu hóa được.

## 4. Phân tích benchmark

- **Layer yếu nhất:** không layer nào fail; điểm yếu là độ trễ — long_term 1634.7ms vs episodic 284.8ms, semantic 574.5ms, do `prime_eval_thread` ghi trước khi đọc.
- **Tốn token nhất:** E08 (1458), E03 (1452), E02 (1428) — đều long_term (Context Block + 20 edges).
- **E07:** cần long_term + semantic; bắt buộc có `Python` và `Idempotency-Key`. Budget cắt long_term 1471 → 324 token, semantic giữ 148.
- **Token reduction:** 14.2% vs 81.8% của no-memory. Baseline tiết kiệm vì không lấy gì, trả giá bằng 2/11 — chỉ có nghĩa khi đọc kèm hit rate.

## 5. E08 và E10

**E08:** graph giữ cả fact cũ (Python) lẫn mới (TypeScript + NestJS); `scope="edges"` trả `valid_at`/`invalid_at` nên fact cũ hết hiệu lực chứ không bị xóa — recency thắng mà vẫn truy vết được.

**E10:** sau 8 compaction còn 6 message (195 token) vẫn giữ `REVIEW-DEADLINE-1600` nhờ 2 durable note; buffer thì token tăng tuyến tính đến khi vỡ context.
