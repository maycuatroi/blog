- Điều gì xảy ra khi một Inmate mới được thêm vào hệ thống?
- Điều gì xảy ra khi một Inmate bị xóa khỏi hệ thống?
- Điều gì xảy ra khi một Inmate được chuyển đến một cell khác?

## System architecture

- High level:
  - 3-tier architecture
    - Presentation tier: User Interface
    - Application tier: Web Server, API Server
    - Data tier: Database, Message Queue
- Presentation tier:
  - User Web Interface
  - Admin Web Interface
- Application tier:
  - Web Server: Nginx
  - API Server: Django/Django Rest Framework
- Data tier:
  - Database: PostgreSQL
  - Message Queue: Kafka
- Deployment:
  - Sử dụng Docker containers cho tất cả các thành phần
  - Triển khai Kubernetes để orchestration container
  - Sử dụng GitLab CI/CD cho continuous integration và deployment
  - Triển khai chiến lược blue-green deployment để cập nhật không có thời gian chết
- Disaster recovery:
  - Thực hiện sao lưu thường xuyên cho tất cả dữ liệu và cấu hình
  - Thiết lập data center hoặc cloud region thứ cấp để failover
  - Tạo và duy trì kế hoạch disaster recovery chi tiết
  - Tiến hành diễn tập disaster recovery thường xuyên
- Security:
  - Triển khai mã hóa SSL/TLS cho tất cả các giao tiếp mạng
  - Sử dụng OAuth 2.0 và JWT cho authentication và authorization
  - Triển khai role-based access control (RBAC)
  - Kiểm tra bảo mật và penetration testing thường xuyên
  - Triển khai phân đoạn mạng và firewalls
- Monitoring:
  - Sử dụng Prometheus để thu thập metrics
  - Triển khai Grafana để visualization và dashboards
  - Thiết lập cảnh báo sử dụng Alertmanager
  - Triển khai distributed tracing với Jaeger
- Logging:
  - Logging tập trung sử dụng ELK stack (Elasticsearch, Logstash, Kibana)
  - Triển khai chính sách log rotation và retention
  - Thiết lập phân tích log và cảnh báo
- Backup:
  - Thực hiện sao lưu incremental hàng ngày và sao lưu đầy đủ hàng tuần
  - Sử dụng công cụ sao lưu tích hợp của PostgreSQL để sao lưu database
  - Lưu trữ bản sao lưu ở vị trí vật lý riêng biệt hoặc cloud storage
  - Thường xuyên kiểm tra quy trình khôi phục bản sao lưu
- Maintenance:
  - Lên lịch các cửa sổ bảo trì thường xuyên để cập nhật và vá lỗi
  - Triển khai kiểm tra sức khỏe hệ thống tự động
  - Tạo runbooks cho các tác vụ bảo trì phổ biến
  - Tiến hành điều chỉnh và tối ưu hóa hiệu suất thường xuyên

## Module

- Camera configuration module:

  - Thêm camera mới
  - Xóa camera
  - Chỉnh sửa camera
  - Xem camera
  - Gán camera cho một task
  - Xem camera stream

- AI Agents Module:
  - Core AI Engine service:
    - AI models:
      - Face Recognition
      - Skeleton Detection
      - Object Segmentation
      - Object Detection
      - Activity Recognition
    - AI Data flow:
      - Input: Camera stream
      - Output: AI models' results
  - AI Agents Manager:
    - Task scheduling:
      - Assign task to AI Agents
    - Task monitoring on Agent:
      - Monitor task status
    - Task result:
      - Collect task results from AI Agents
- Logical components:

  - Đánh nhau, vật nhau
  - Tụ tập đông người, bạo lực
  - Hành vi không chế tấn công cán bộ quản giáo
  - Hành vi khống chế cán bộ gác cổng cơ quan, cổng khu giam (gương mặt lạ xâm nhập khu vực cấm)
  - Mài các vật sắc nhọn
  - Hành động tự thương: Treo cổ tự tử
  - Hành động tự thương: Đập đầu vào tường
  - Trèo lên cửa, vị trí trên cao cắm đầu xuống đất
  - Cắt vào cổ, cứa cổ tay, cổ chân
  - Rút chỉ, se dây dài
  - Xé quần áo, chăn màn
  - Chói tay, chói chân
  - Cửa cùm
  - Đào, đục tường
  - Bác thang, leo trèo qua tường rào bảo vệ Trại
  - Mặc dân sự đi lại trong hành lang, trong khu giam, trong trường chòi, qua cổng khu giam
  - Thông cung
  - Các đối tượng nằm ngủ thời gian trên 2h00 không cử động
  - Nhận dạng vết máu, máu chảy nền nhà
  - Hành vi ngã (đột quỵ)
  - Có lửa
  - Hút thuốc
  - Phát hiện UAV trong khu vực

- Container management module:

  - Cập nhật model
  - Cập nhật container

- Face recognition with Vector Database:

  - Vector Database:Milvus
    - For each face, we will store its vector representation in the vector database.
    - Use the vector database to perform face recognition tasks with additional query information such as:
      - Face vector
      - Camera ID
      - Time
      - Cell

- Task scheduler:

  - Gán task and Camera cho AI Agents
  - Xem trạng thái task
  - Xem kết quả task
  - Xem log task

- Master service:
  - Quản lý Cells
  - Quản lý Inmates
  - Quản lý Cameras
  - Quản lý Tasks
  - Quản lý AI models
  - Quản lý Containers
  - Quản lý Users
  - Quản lý Roles
  - Quản lý Permissions
  - Quản lý Logs
  - Quản lý Alerts
  - Quản lý Reports
  - Quản lý Settings
  - Quản lý Notifications
  - Quản lý Integrations
  - Quản lý API
- User interface:

  - User Web Interface
  - Admin Web Interface

- Message queue integration:

  - Kafka

- Chia thành 3 loại phát hiện:
  - Phát hiện thời gian thực < 3s
  - Phát hiện gần thời gian thực < 2 phút
  - Phát hiện offline > 2 phút
- Giao diện người dùng cho các kịch bản trên là gì?

  - Phát hiện thời gian thực:
    - Hiển thị góc nhìn trực tiếp từ camera
    - Hiển thị kết quả phát hiện trong góc nhìn camera
    - Hiển thị kết quả phát hiện trong bảng với các thông tin sau:
      - ID Inmate
      - Tên Inmate
      - Cell
      - Thời gian
      - Hành động:
        - Cảnh báo
        - Đã phát hiện
        - Không phát hiện
  - Phát hiện gần thời gian thực:
    - Hiển thị kết quả phát hiện trong bảng với các thông tin sau:
      - ID Inmate
      - Tên Inmate
      - Cell
      - Thời gian
      - Hành động:
        - Cảnh báo
        - Đã phát hiện
        - Không phát hiện
  - Phát hiện offline:
    - Hiển thị kết quả phát hiện trong bảng với các thông tin sau:
      - ID Inmate
      - Tên Inmate
      - Cell
      - Thời gian
      - Hành động:
        - Cảnh báo
        - Đã phát hiện
        - Không phát hiện

- Packaging và deployment:
  - Docker
  - CI
    - Gitlab Runner
  - CD
    - Làm thế nào để triển khai lên server cực kỳ riêng tư?

## High Availability và Backup Strategy

### 1. Database Replication

- Thiết lập PostgreSQL với primary-secondary replication.
  - Apache Flink
- Triển khai failover tự động sang secondary database nếu primary bị lỗi.

### 2. Message Queue Clustering

- Triển khai Kafka trong cấu hình multi-broker cluster.
- Triển khai Zookeeper Kafka cluster.

### 3. AI Agent Redundancy

- Triển khai nhiều node AI Agent với load balancing.
- Triển khai cơ chế heartbeat để phát hiện các node AI Agent bị lỗi.
- Tự động gán lại các task từ các node bị lỗi sang các node healthy.

### 4. Backup and Recovery

- Triển khai kế hoạch disaster recovery với các quy trình từng bước để khôi phục hệ thống.

### 5. Health monitoring and Alerting

- Using Prometheus/Grafana to monitor system health
- Setup alerting for system critical metrics, component errors and performance issues.
- Create on-call schedule to respond to important alerts immediately.

### 6. Graceful Degradation

- Design system to continue operation with reduced capability if non-critical components fail.
- Implement fallback mechanism for AI processing if some AI models or services are unavailable.

### 7. Data Synchronization

- Implement robust data synchronization mechanism when switching between primary and secondary systems.

### 9. Containerization và Orchestration

- Sử dụng Docker containers để dễ dàng triển khai và mở rộng các thành phần hệ thống.
- Triển khai Kubernetes để orchestration container, cho phép tự động re-schedule các container bị lỗi.
