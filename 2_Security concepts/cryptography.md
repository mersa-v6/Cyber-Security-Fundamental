# **cryptography**

the is a concept applied in cybersecurity solutions like :

- [Cisco Security](https://gblogs.cisco.com/ca/2020/08/26/the-canadian-bacon-cisco-security-and-the-pyramid-of-pain/)
- [SentinelOne](https://www.sentinelone.com/blog/revisiting-the-pyramid-of-pain-leveraging-edr-data-to-improve-cyber-threat-intelligence/)
- [SOCRadar](https://socradar.io/re-examining-the-pyramid-of-pain-to-use-cyber-threat-intelligence-more-effectively/)

To improve the effectiveness of 

- cti → Cyber Threat Intelligence
- threat hunting
- incident response exercises

## Hashing التجزئه

هي عمليه نحويل اي نص مهما كان حجمه الي مفتاح او hashing text 

وهو عباره عن fixed length 

- Irreversible → one way function
- fixed output size
- example:  md4 , md5 , sha1 , sha2

***اهميته*** 

يستخدم لتاكيد ان الملف مثلا لم يتم تغيره او التلاعب فيه عشان انا بعمله هاش عند ارساله وبرسل مفتاح بتاعت الهاش دي 

ولما الطرف التاني يستلم الملف بيعمله هاشينج بردو ويقارن المفتاحين ببعض لو متماثلين تمام لو مختلفين يبقي تم التلاعب فيها 

## Encoding الترميز

هو باختصار تحويل لفه مفهومه بالنسبه الي لغه اخري مفهومه بالنسبه لحهه اخري 

عند تحويل النصوص علي الكمبيوتر الي بيناري 0و1 عشان هيفهمها الكمبيوتر فلما الكمبيوتر يفهمها وبعدين يحولها تاني الي نصوص يبقي عملها 

decoding

Example:

- base 64
- url
- html

## Encryption التشفير