# OSI Layer

[ Open System Interconnection ]

![daw7e0lj.bmp](Cyber%20Security%20369db91137f44179916e0f47855d6dd7/daw7e0lj.bmp)

- 7- Application Function Layer
    
    هي المرحله التي يتعامل فيها مع المتصفح واطلب مثلا جوجل في المتصفح , بيبدا اللمتصفح يشوف البروتوكول المناسب لعمليه طلب السيرفر دا 
    
    [www.google.com](http://www.google.com) → https://www.google.com
    
    فمثلا بستخدم http او ftp حسب الاحتياج 
    
    - resolve hostname
    - get ip from dns
    
     
    
- 6 - Presentation Function Layer
    
    مرحله تجهيز الريكويست والملفات من ضغط لتشفير وفك ضغط وتشفير وتحديد امتداد الملفات 
    
    بيبدا برتوكول TLS [ SSL ]
    
    بتشفير http ماعدا الاي بي وبعض المعلومات الاخري 
    
    > HTTP Request → Get ip from DNS → ssl → HTTPS
    > 
- 5 - Sessions Function Layer
    
    asking [os] for creating network socket port 
    
    بيبدا المتصفح باخد الريكويست ويسال النظام بفتح منفذ 
    
- 4 - Transport Function Layer
    
    هو الطبقه المسؤله عن اداره البيانات flow control 
    
    وبيبدا بنقل المعلومات وبيبدا يقسم الباكيت الي سيكوانسيس لو كبيره 
    
    > [HTTP DATA + TCP HEADER ]
    > 
    
    ![Untitled](Cyber%20Security%20369db91137f44179916e0f47855d6dd7/Untitled%201.png)
    
- 3 - Network Function Layer
    
    بعد الطبقه السابقه الي هي كانت عباره عن segment 
    
    هتتحول هنا الي باكيت في tcp 
    
    كانت محطوط بورت فقط لاكن هنا هنبدا احدد الاي بي للشخص والسيرفر عن طريقه الراوتينج 
    
    > ip + tcp header + https req
    > 
- 2 - DataLink Function Layer
    
    تسمي الداتا لينك بطبقه ال farm 
    
    اطار يعني عشان يتحط راس الداتا وديل للداتا 
    
    الديل والراس اسمهم Ethernet Protocol
    
- 1 - Physical Function Layer
    
    هي المرحه التي التي يتم فيها تحول الداتا من fram 
    
    الي ف اخر layer 
    
    الي اشارت bits 
    
    ويقوم بهذه الوظيفه NIC والاسلاك 
    

## SUMMARY :

Browser → url → http → Get ip → SSL → Https →[ Https + tcp ]→[ https + tcp + ip ]→ [ Ethernet head  ] → [ ip + tcp + https + footer ] → [ Cables + router ] 