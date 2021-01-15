## Your Friendship Destroyer

> Multiplay "connect four" with your friends !

Note:

+ This project is powered by Flask, so essential Python runtime environment is required to run it.
  + Flask
  + yaml

---

To do List:

+ 游戏整体逻辑
+ 每隔3s改成重载部分 √
+ 你需要对整体的游戏加载和编辑进程进行大规模的重构。
  + 我们不能在zeit上运行这款游戏，现在的要求是只需要在本地能够跑起来就可以。
  + 所以，尽可能的压榨这37ms 的时间是非常有必要的。
  + 作为重构任务，你需要把游戏存储从mass storage 移动到 memory 中
  + 我们必须解决 “ 另一个程序正在使用此文件，进程无法访问。” 的问题
    + 可以增加bool检验变量，防止脏读
    + => 全局变量体系必须建立！



**对了，我们有一个特性，就是在你下每一手棋之前，会给你充分多的考虑时间。**

By the way, it is a feature that we'll give you more than enough time to think before you make your decision every turn.

**这个特性是 Beta 20210114 版本引入游戏的.**

This feature is added on Thursday, Jan 14, 2021.

**我们在 Beta 20210115 版本又加入了一个特性，那就是棋盘可能会影分身，我也不知道为什么。**

We added another feature in version Beta 20210115 that while playing games and refreshing your chess table, your table may duplicate itself. I have no idea why it should work like that.

**不管怎样，我要先把这辣鸡代码传到 Github 上面，然后自己再重构。**

Anyway, I'm now going to upload this SHIT code to Gayhub and try to be a Pigeon.
Maybe in a few days these bugs will fix themselves.
Believe it or not, I'm 99% positive that it'd be realized.

This line is used to test VScode-Gayhub Link.