# python_youtube
youtube视频数据分析python
基于Django框架搭建


公共url地址：
    /my_test/v1
获取视频喜欢不喜欢比率接口地址：
    /get
参数为rate
当参数tate的值为空或者没有参数时，返回结果为

{"data": [{"_id": "2kyS6SvSYSE","index": 0,"name": "WE WANT TO TALK ABOUT OUR MARRIAGE","like_rate": 91.72},{"_id": "1ZAPwfrtAFY","index": 1,"name": "The Trump Presidency: Last Week Tonight with John Oliver (HBO)","like_rate": 92.39},{"_id": "5qpjK5DgCt4","index": 2,"name": "Racist Superman | Rudy Mancuso, King Bach & Lele Pons","like_rate": 96.11},{"_id": "puqaWrEC7tY","index": 3,"name": "Nickelback Lyrics: Real or Fake?","like_rate": 91.71},{"_id": "d380meD0W0M","index": 4,"name": "I Dare You: GOING BALD!?","like_rate": 98.42},{"_id": "gHZ1Qz0KiKM","index": 5,"name": "2 Weeks with iPhone X","like_rate": 87.62},{"_id": "39idVpFF7NQ","index": 6,"name": "Roy Moore & Jeff Sessions Cold Open - SNL","like_rate": 83.94},{"_id": "nc99ccSXST0","index": 7,"name": "5 Ice Cream Gadgets put to the Test","like_rate": 96.04},{"_id": "jr9QtXwC9vc","index": 8,"name": "The Greatest Showman | Official Trailer 2 [HD] | 20th Century FOX","like_rate": 96.02}],"status": 200,"msg": "success"}

当参数tate的值为above时，返回结果为

{"data": [{"_id": "5qpjK5DgCt4","index": 2,"name": "Racist Superman | Rudy Mancuso, King Bach & Lele Pons","like_rate": 96.11},{"_id": "d380meD0W0M","index": 4,"name": "I Dare You: GOING BALD!?","like_rate": 98.42},{"_id": "nc99ccSXST0","index": 7,"name": "5 Ice Cream Gadgets put to the Test","like_rate": 96.04},{"_id": "jr9QtXwC9vc","index": 8,"name": "The Greatest Showman | Official Trailer 2 [HD] | 20th Century FOX","like_rate": 96.02}],"status": 200,"msg": "success"}

当参数tate的值为below时，返回结果为

{"data": [{"_id": "2kyS6SvSYSE","index": 0,"name": "WE WANT TO TALK ABOUT OUR MARRIAGE","like_rate": 91.72},{"_id": "1ZAPwfrtAFY","index": 1,"name": "The Trump Presidency: Last Week Tonight with John Oliver (HBO)","like_rate": 92.39},{"_id": "puqaWrEC7tY","index": 3,"name": "Nickelback Lyrics: Real or Fake?","like_rate": 91.71},{"_id": "gHZ1Qz0KiKM","index": 5,"name": "2 Weeks with iPhone X","like_rate": 87.62},{"_id": "39idVpFF7NQ","index": 6,"name": "Roy Moore & Jeff Sessions Cold Open - SNL","like_rate": 83.94}],"status": 200,"msg": "success"}

当参数tate的值为likes时，返回结果为

{"data": [{"_id": "1ZAPwfrtAFY","index": 1,"name": "The Trump Presidency: Last Week Tonight with John Oliver (HBO)","like_num": 151250,"like_rate": 92.39},{"_id": "5qpjK5DgCt4","index": 2,"name": "Racist Superman | Rudy Mancuso, King Bach & Lele Pons","like_num": 187303,"like_rate": 96.11},{"_id": "d380meD0W0M","index": 4,"name": "I Dare You: GOING BALD!?","like_num": 153395,"like_rate": 98.42}],"status": 200,"msg": "success"}

返回结果字段解释：
 
