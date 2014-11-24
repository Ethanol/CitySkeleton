City Skeleton 城市骨骼
============
这是一个2013年的项目。

闲来无事利用 Python 和 BeautifulSoup 在 8684.cn 上抓取了公交线路和站点信息，然后用 Gephi 画出了站点之间的拓扑结构并用了自带的 Force Altas 算法做了处理，算是假期的无聊消遣。代码写的 quick and dirty，因为爬虫最大的时间都耗在了抓取时间上，本身算法的效率并不是决定性的因素。

代码按照1~4来执行。但是由于后来 8684.cn网站的架构发生了变化，第一部分的代码已经不能用了。代码中有一些细节处理，如抓取动作的时间间隔，不过整体上讲非常常规。

---

我是一个对城市很感兴趣的人，城市的历史、发展和流动，背后是城市的特色和风格。这次利用公交刻画城市，画出的正是城市人的群像。公交的站点之间的线路，也就是这两个点的时间距离、人流距离。不过我没办法获得每条线路的人流，所以只能用这个粗放的方式作为初步的实践。[BCL](http://www.beijingcitylab.com/) 做过一系列的公交可视化，因为数据更多，所以看起来更震撼。

这里做出来的结果，一定程度上反映了城市分区和发展的大体脉络。这种城市的抽象，完成了城市形象某个角度的构建，虽然是抽象的线图，但是仍有城市不可磨灭的印记。

#### 北京
北京的骨骼中，最粗壮的那一条是三环，北四环也跟北三环紧紧贴在了一起。还能明显看到北京的几个郊县卫星城。
![Beijing](http://multisim.me/media/images/beijing.png)

#### 上海
上海跟北京相反，因为地形和发展的关系，郊县的联系相对紧密。
![Shanghai](http://multisim.me/media/images/shanghai.png)

#### 香港
连接港岛和九龙的桥。
![Hongkong](http://multisim.me/media/images/hongkong.png)

#### 成都
明显的环路和都江堰。
![Chengdu](http://multisim.me/media/images/chengdu.png)

#### 兰州
线性的兰州。
![Lanzhou](http://multisim.me/media/images/lanzhou.png)

#### 南京
有南京人说从这里看到了长江大桥。我不熟悉，看不见。
![Nanjing](http://multisim.me/media/images/nanjing.png)

#### 厦门
岛屿。
![Xiamen](http://multisim.me/media/images/xiamen.png)
