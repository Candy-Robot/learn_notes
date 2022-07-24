## 什么是HTML?

HTML 是用来描述网页的一种语言。

- HTML 指的是超文本标记语言: **H**yper**T**ext **M**arkup **L**anguage
- HTML 不是一种编程语言，而是一种**标记**语言
- 标记语言是一套**标记标签** (markup tag)
- HTML 使用标记标签来**描述**网页
- HTML 文档包含了HTML **标签**及**文本**内容
- HTML文档也叫做 **web 页面**

![02A7DD95-22B4-4FB9-B994-DDB5393F7F03](https://www.runoob.com/wp-content/uploads/2013/06/02A7DD95-22B4-4FB9-B994-DDB5393F7F03.jpg)

## HTML 标签

HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

- HTML 标签是由*尖括号*包围的关键词，比如 <html>
- HTML 标签通常是*成对出现*的，比如 <b> 和 </b>
- 标签对中的第一个标签是*开始标签*，第二个标签是*结束标签*
- 开始和结束标签也被称为*开放标签*和*闭合标签*

<标签>内容</标签>



## HTML基础

~~~html
HTML 标题（Heading）是通过<h1> - <h6> 标签来定义的。
<h1>这是一个标题</h1>
  
HTML 段落是通过标签 <p> 来定义的。
<p>这是一个段落。</p>
  
HTML 链接是通过标签 <a> 来定义的。
<a href="https://www.runoob.com">这是一个链接</a>
  
HTML 图像是通过标签 <img> 来定义的.
<img src="/images/logo.png" width="258" height="39" />
~~~

## HTML 元素

- HTML 元素以**开始标签**起始
- HTML 元素以**结束标签**终止
- **元素的内容**是开始标签与结束标签之间的内容
- 某些 HTML 元素具有**空内容（empty content）**
- 空元素**在开始标签中进行关闭**（以开始标签的结束而结束）
- 大多数 HTML 元素可拥有**属性**

不要忘记结束标签

没有内容的HTML元素被称为空元素。

尽量使用小写标签

## HTML属性

- HTML 元素可以设置**属性**
- 属性可以在元素中添加**附加信息**
- 属性一般描述于**开始标签**
- 属性总是以名称/值对的形式出现，**比如：name="value"**。

HTML 链接由 <a> 标签定义。链接的地址在 **href 属性**中指定：

实例

~~~ html
<a href="http://www.runoob.com">这是一个链接</a>
~~~

## HTML 水平线

<hr> 标签在 HTML 页面中创建水平线。

hr 元素可用于分隔内容。

实例

<p>这是一个段落。</p> <hr> <p>这是一个段落。</p> <hr> <p>这是一个段落。</p>

## HTML 注释

可以将注释插入 HTML 代码中，这样可以提高其可读性，使代码更易被人理解。浏览器会忽略注释，也不会显示它们。

注释写法如下:

 实例

<!-- 这是一个注释 -->

## HTML 折行

如果您希望在不产生一个新段落的情况下进行换行（新行），请使用 **<br>** 标签：

 实例

<p>这个<br>段落<br>演示了分行的效果</p>

## HTML 文本格式化标签

| 标签                                                     | 描述         |
| :------------------------------------------------------- | :----------- |
| [<b>](https://www.runoob.com/tags/tag-b.html)            | 定义粗体文本 |
| [<em>](https://www.runoob.com/tags/tag-em.html)          | 定义着重文字 |
| [<i>](https://www.runoob.com/tags/tag-i.html)            | 定义斜体字   |
| [<small>](https://www.runoob.com/tags/tag-small.html)    | 定义小号字   |
| [<strong>](https://www.runoob.com/tags/tag-strong.html)  | 定义加重语气 |
| [<sub>](https://www.runoob.com/tags/tag-sub.html)        | 定义下标字   |
| [<sup>](https://www.runoob.com/html/m/tags/tag-sup.html) | 定义上标字   |
| [<ins>](https://www.runoob.com/tags/tag-ins.html)        | 定义插入字   |
| [<del>](https://www.runoob.com/tags/tag-del.html)        | 定义删除字   |

## HTML 链接语法

链接的 HTML 代码很简单。它类似这样：

~~~html
<a href="url">链接文本</a>
~~~

href 属性描述了链接的目标。.

 实例

~~~html
<a href="https://www.runoob.com/">访问菜鸟教程</a>
~~~

上面这行代码显示为：[访问菜鸟教程](https://www.runoob.com/)

点击这个超链接会把用户带到菜鸟教程的首页。

**提示:** *"链接文本"* 不必一定是文本。图片或其他 HTML 元素都可以成为链接。

## CSS

用来渲染HTML元素

CSS 是在 HTML 4 开始使用的,是为了更好的渲染HTML元素而引入的.

CSS 可以通过以下方式添加到HTML中:

- 内联样式- 在HTML元素中使用"style" **属性**
- 内部样式表 -在HTML文档头部 <head> 区域使用<style> **元素** 来包含CSS
- 外部引用 - 使用外部 CSS **文件**

最好的方式是通过外部引用CSS文件.

## HTML 框架

------

通过使用框架，你可以在同一个浏览器窗口中显示不止一个页面。
