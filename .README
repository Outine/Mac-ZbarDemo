You might need a few dependencies from brew, figure it out, it worked for me from things I had previously installed. 
Then compile with these cflags, as it will make the ./configure look at the brew directories. 

CPPFLAGS="-I/opt/local/include" LDFLAGS="-L/opt/local/lib" ./configure --disable-video --without-qt --without-python --without-gtk --with-libiconv-prefix=/opt/local --with-jpeg=yes --with-python=yes

https://mousecradle.wordpress.com/2012/06/22/compiling-zbar-on-osx/

http://blog.ayoungprogrammer.com/2013/07/tutorial-scanning-barcodes-qr-codes.html

You need to get ZBar from sourceforge, and then patch it, or the python bindings segfault;
Make the change described here - 
https://github.com/npinchot/zbar/commit/d3c1611ad2411fbdc3e79eb96ca704a63d30ae69

And compile and install zbar. 

Then my demos should work, but only on Mac with isight webcam or something. 
