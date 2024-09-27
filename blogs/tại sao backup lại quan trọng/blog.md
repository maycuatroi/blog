# Hành trình xây dựng module backup hiệu quả: Bài học từ dự án BigQuery

Khi tôi được giao nhiệm vụ thiết kế hệ thống tối ưu hóa cho một công ty hàng đầu trong lĩnh vực, tôi đã rất phấn khích. Đây là cơ hội lớn để tôi va team thể hiện khả năng và kiến thức của mình. Ban đầu, tôi tập trung vào những vấn đề phức tạp như kiến trúc hệ thống, xử lý dữ liệu lớn và tối ưu hóa hiệu suất. Trong quá trình này, tôi đã bỏ qua một khía cạnh quan trọng mà tôi cho rằng đã có sẵn giải pháp: vấn đề backup dữ liệu.

Tôi đã nghĩ rằng backup là một bài toán "mặc định" trong bất kỳ dự án nào. Với suy nghĩ này, tôi đã không dành nhiều thời gian để nghiên cứu sâu về nhu cầu backup cụ thể của dự án. Tôi tự tin rằng có thể áp dụng các giải pháp có sẵn một cách dễ dàng. 

Khi đó với bản prototype, tôi đọc qua ý tưởng from business user và đưa ra nhận định ban đầu với mong muốn của bussiness user về backup sẽ liên quan nhiều đến việc khi một session chạy bị lỗi hoặc downtime không mong muốn thì có thể recovery để chạy lại. Hoặc là để thực hiện những investigation ngắn hạn với data gần đây. Khi đó, sử dụng trực tiếp bigquery time travel là đủ (thật vậy nếu bạn chỉ cần backup trong thời gian ngắn thì vậy là đủ, hãy dành thời gian đi improve các module khác).

Câu chuyện này sẽ cho bạn thấy rằng trong lĩnh vực công nghệ, đặc biệt là AI, không có gì là "mặc định" cả. Mỗi dự án đều có những yêu cầu riêng biệt, và việc backup dữ liệu cũng không ngoại lệ. Hãy cùng tôi khám phá hành trình học hỏi và xây dựng một giải pháp backup hiệu quả cho dự án này.

## Bài học đầu tiên: Lắng nghe và hiểu rõ nhu cầu

Ngày hôm đó, tôi bước vào phòng họp với tâm trạng hào hứng. Trong tay là bản thuyết trình về giải pháp backup mà tôi đã chuẩn bị kỹ lưỡng suốt mấy tuần qua. Tôi tự tin rằng đề xuất sử dụng tính năng time-travel của BigQuery sẽ giải quyết mọi vấn đề. Nhưng rồi...

"Chúng tôi cần backup dữ liệu ít nhất 2 năm."

Câu nói của vị khách hàng như một gáo nước lạnh dội thẳng vào mặt tôi. Tôi chết lặng. Giải pháp của tôi chỉ có thể backup được 7 ngày. Tôi đã quá ngây thơ và đánh giá sai hoàn toàn yêu cầu của khách hàng.

## Bài học đầu tiên: Lắng nghe và hiểu rõ nhu cầu

Qua sự cố này, tôi nhận ra rằng việc lắng nghe và hiểu rõ nhu cầu dài hạn của khách hàng là vô cùng quan trọng. Tôi đã quá vội vàng đưa ra giải pháp mà không tìm hiểu kỹ yêu cầu thực sự.

Sau cuộc họp đó, tôi bắt đầu nghiên cứu kỹ hơn về nhu cầu backup của khách hàng. Tôi phát hiện ra rằng:

1. Mỗi ngày có hơn 500 session chạy cho nhiều quốc gia khác nhau.
2. Cần lưu lại toàn bộ dữ liệu của mỗi session để phân tích và giải thích kết quả khi có yêu cầu.
3. Dữ liệu backup cực kỳ quan trọng cho việc back-test, đánh giá hiệu quả của những cải tiến trong hệ thống AI.

## Thách thức và giải pháp

Với những yêu cầu này, tôi nhận ra có 3 thách thức chính:

1. Dữ liệu mỗi session rất lớn và có nhiều sự chùng lặp.
2. Cần một giải pháp lưu trữ backup vừa hiệu quả về chi phí, vừa đảm bảo tốc độ truy xuất.
3. Khả năng rollback nhanh chóng khi cần thiết.

Để giải quyết những thách thức này, tôi đã nghiên cứu và đề xuất 3 chiến lược backup chính:

1. Full Backup: Sao lưu toàn bộ dữ liệu mỗi lần.
2. Incremental Backup: Chỉ sao lưu những thay đổi kể từ lần backup gần nhất.
3. Differential Backup: Sao lưu những thay đổi kể từ lần full backup gần nhất.

## Kiến trúc đề xuất

Sau nhiều đêm trăn trở, tôi đề xuất một kiến trúc gồm 5 dataset chính:

1. Data source: Nguồn dữ liệu gốc.
2. Landing dataset: Nơi tập trung dữ liệu từ nhiều nguồn.
3. Processing layer datasets: Xử lý dữ liệu.
4. Result dataset: Lưu trữ kết quả.
5. Backup dataset: Hệ thống backup chính.

Trong đó, Backup dataset được chia làm ba phần:

1. Head tables: Lưu trữ dữ liệu mới nhất, dễ dàng truy cập.
2. History tables: Lưu trữ dữ liệu lịch sử gần đây.
3. Cold History Storage: Lưu trữ dữ liệu lâu dài, ít được truy cập.

## Bài học cuối cùng: Đơn giản hóa là chìa khóa

Khi trình bày giải pháp mới này với khách hàng, tôi nhớ đến lời khuyên của một người thầy cũ: "Hãy viết như thể bạn đang viết một cuốn sách tranh cho trẻ em" [1].

Thay vì sử dụng những thuật ngữ phức tạp, tôi cố gắng diễn đạt ý tưởng bằng những từ ngữ đơn giản nhất. Tôi sử dụng nhiều hình ảnh minh họa và biểu đồ để làm rõ ý tưởng. Kết quả là khách hàng hiểu rõ và đồng ý với đề xuất của tôi.

## Kết luận

Hành trình xây dựng module backup hiệu quả này đã cho tôi nhiều bài học quý giá. Từ suy nghĩ ngây thơ ban đầu đến việc đối mặt với thực tế phức tạp, tôi đã học được rằng trong lĩnh vực AI và xử lý dữ liệu lớn, việc backup không chỉ đơn thuần là "sao lưu để phòng khi có sự cố". Nó là một phần quan trọng trong việc đảm bảo tính minh bạch, khả năng giải thích và cải tiến liên tục của hệ thống.

Hy vọng qua câu chuyện của tôi, các bạn có thể rút ra được những bài học hữu ích cho dự án của mình. Hãy nhớ rằng, trong thế giới công nghệ luôn thay đổi, việc học hỏi và thích nghi là chìa khóa để thành công.

[1] https://forum.effectivealtruism.org/posts/vYGHzKocbaEcsSfdp/your-next-forum-post-should-be-more-like-a-children-s-book
