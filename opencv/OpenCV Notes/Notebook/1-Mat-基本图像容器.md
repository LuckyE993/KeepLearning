[OpenCV官方文档 Mat - The Basic Image Container](https://docs.opencv.org/4.8.0/d6/d6d/tutorial_mat_the_basic_image_container.html)
这部分主要介绍了OpenCV中如何表示图像，以及Mat的存储格式。

首先，Mat格式在OpenCV中只是一个标头，并不占用实际存储空间。只有在使用`clone`或`copyTo`函数时，才会完整复制整个矩阵。否则，Mat对象仅作为一个指针，指向相同的内容。

接着，内容涉及了图像色彩的存储方式，如RGB、BGR等。其中，BGR是OpenCV中最常用的存储方式。

随后介绍了显式创建Mat对象的方法。你可以创建多通道矩阵，指定输出格式，支持多种格式（如默认格式、Python格式、CSV、NumPy等），这些都可以通过`format()`函数来实现。