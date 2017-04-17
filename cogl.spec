#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cogl
Version  : 1.22.2
Release  : 8
URL      : http://ftp.gnome.org/pub/gnome/sources/cogl/1.22/cogl-1.22.2.tar.xz
Source0  : http://ftp.gnome.org/pub/gnome/sources/cogl/1.22/cogl-1.22.2.tar.xz
Summary  : A 2D path drawing library for Cogl
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1 MIT
Requires: cogl-lib
Requires: cogl-data
Requires: cogl-locales
BuildRequires : cairo-dev
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(glesv1_cm)
BuildRequires : pkgconfig(glesv2)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(sdl)
BuildRequires : pkgconfig(sdl2)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xrandr)

%description
/*
*/
General Polygon Tesselation
---------------------------
This note describes a tesselator for polygons consisting of one or
more closed contours.  It is backward-compatible with the current
OpenGL Utilities tesselator, and is intended to replace it.  Here is
a summary of the major differences:

%package data
Summary: data components for the cogl package.
Group: Data

%description data
data components for the cogl package.


%package dev
Summary: dev components for the cogl package.
Group: Development
Requires: cogl-lib
Requires: cogl-data
Provides: cogl-devel

%description dev
dev components for the cogl package.


%package lib
Summary: lib components for the cogl package.
Group: Libraries
Requires: cogl-data

%description lib
lib components for the cogl package.


%package locales
Summary: locales components for the cogl package.
Group: Default

%description locales
locales components for the cogl package.


%prep
%setup -q -n cogl-1.22.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491313828
%configure --disable-static --enable-cogl-gles2=yes \
--enable-gles2=yes \
--enable-gl=yes \
--enable-wayland-egl-platform=yes \
--enable-wayland-egl-server=yes
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1491313828
rm -rf %{buildroot}
%make_install
%find_lang cogl

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Cogl-1.0.typelib
/usr/lib64/girepository-1.0/Cogl-2.0.typelib
/usr/lib64/girepository-1.0/CoglPango-1.0.typelib
/usr/lib64/girepository-1.0/CoglPango-2.0.typelib
/usr/share/cogl/examples-data/crate.jpg
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/cogl/cogl-gles2/GLES2/gl2.h
/usr/include/cogl/cogl-gles2/GLES2/gl2ext.h
/usr/include/cogl/cogl-gles2/GLES2/gl2platform.h
/usr/include/cogl/cogl-pango/cogl-pango.h
/usr/include/cogl/cogl-path/cogl-path-enum-types.h
/usr/include/cogl/cogl-path/cogl-path-types.h
/usr/include/cogl/cogl-path/cogl-path.h
/usr/include/cogl/cogl-path/cogl1-path-functions.h
/usr/include/cogl/cogl-path/cogl2-path-functions.h
/usr/include/cogl/cogl/cogl-atlas-texture.h
/usr/include/cogl/cogl/cogl-attribute-buffer.h
/usr/include/cogl/cogl/cogl-attribute.h
/usr/include/cogl/cogl/cogl-auto-texture.h
/usr/include/cogl/cogl/cogl-bitmap.h
/usr/include/cogl/cogl/cogl-buffer.h
/usr/include/cogl/cogl/cogl-clip-state.h
/usr/include/cogl/cogl/cogl-clutter-xlib.h
/usr/include/cogl/cogl/cogl-clutter.h
/usr/include/cogl/cogl/cogl-color.h
/usr/include/cogl/cogl/cogl-context.h
/usr/include/cogl/cogl/cogl-defines.h
/usr/include/cogl/cogl/cogl-deprecated.h
/usr/include/cogl/cogl/cogl-depth-state.h
/usr/include/cogl/cogl/cogl-display.h
/usr/include/cogl/cogl/cogl-egl-defines.h
/usr/include/cogl/cogl/cogl-egl.h
/usr/include/cogl/cogl/cogl-enum-types.h
/usr/include/cogl/cogl/cogl-error.h
/usr/include/cogl/cogl/cogl-euler.h
/usr/include/cogl/cogl/cogl-fence.h
/usr/include/cogl/cogl/cogl-fixed.h
/usr/include/cogl/cogl/cogl-frame-info.h
/usr/include/cogl/cogl/cogl-framebuffer-deprecated.h
/usr/include/cogl/cogl/cogl-framebuffer.h
/usr/include/cogl/cogl/cogl-gles2-types.h
/usr/include/cogl/cogl/cogl-gles2.h
/usr/include/cogl/cogl/cogl-glib-source.h
/usr/include/cogl/cogl/cogl-glx.h
/usr/include/cogl/cogl/cogl-index-buffer.h
/usr/include/cogl/cogl/cogl-indices.h
/usr/include/cogl/cogl/cogl-macros.h
/usr/include/cogl/cogl/cogl-material-compat.h
/usr/include/cogl/cogl/cogl-matrix-stack.h
/usr/include/cogl/cogl/cogl-matrix.h
/usr/include/cogl/cogl/cogl-meta-texture.h
/usr/include/cogl/cogl/cogl-object.h
/usr/include/cogl/cogl/cogl-offscreen.h
/usr/include/cogl/cogl/cogl-onscreen-template.h
/usr/include/cogl/cogl/cogl-onscreen.h
/usr/include/cogl/cogl/cogl-output.h
/usr/include/cogl/cogl/cogl-pango.h
/usr/include/cogl/cogl/cogl-pipeline-layer-state.h
/usr/include/cogl/cogl/cogl-pipeline-state.h
/usr/include/cogl/cogl/cogl-pipeline.h
/usr/include/cogl/cogl/cogl-pixel-buffer.h
/usr/include/cogl/cogl/cogl-poll.h
/usr/include/cogl/cogl/cogl-primitive-texture.h
/usr/include/cogl/cogl/cogl-primitive.h
/usr/include/cogl/cogl/cogl-primitives.h
/usr/include/cogl/cogl/cogl-quaternion.h
/usr/include/cogl/cogl/cogl-renderer.h
/usr/include/cogl/cogl/cogl-shader.h
/usr/include/cogl/cogl/cogl-snippet.h
/usr/include/cogl/cogl/cogl-sub-texture.h
/usr/include/cogl/cogl/cogl-swap-chain.h
/usr/include/cogl/cogl/cogl-texture-2d-gl.h
/usr/include/cogl/cogl/cogl-texture-2d-sliced.h
/usr/include/cogl/cogl/cogl-texture-2d.h
/usr/include/cogl/cogl/cogl-texture-3d.h
/usr/include/cogl/cogl/cogl-texture-deprecated.h
/usr/include/cogl/cogl/cogl-texture-pixmap-x11.h
/usr/include/cogl/cogl/cogl-texture-rectangle.h
/usr/include/cogl/cogl/cogl-texture.h
/usr/include/cogl/cogl/cogl-type-casts.h
/usr/include/cogl/cogl/cogl-types.h
/usr/include/cogl/cogl/cogl-vector.h
/usr/include/cogl/cogl/cogl-version.h
/usr/include/cogl/cogl/cogl-vertex-buffer.h
/usr/include/cogl/cogl/cogl-wayland-client.h
/usr/include/cogl/cogl/cogl-wayland-renderer.h
/usr/include/cogl/cogl/cogl-wayland-server.h
/usr/include/cogl/cogl/cogl-xlib-renderer.h
/usr/include/cogl/cogl/cogl-xlib.h
/usr/include/cogl/cogl/cogl.h
/usr/include/cogl/cogl/cogl1-context.h
/usr/include/cogl/cogl/cogl2-experimental.h
/usr/include/cogl/cogl/deprecated/cogl-auto-texture.h
/usr/include/cogl/cogl/deprecated/cogl-clip-state.h
/usr/include/cogl/cogl/deprecated/cogl-clutter-xlib.h
/usr/include/cogl/cogl/deprecated/cogl-clutter.h
/usr/include/cogl/cogl/deprecated/cogl-fixed.h
/usr/include/cogl/cogl/deprecated/cogl-framebuffer-deprecated.h
/usr/include/cogl/cogl/deprecated/cogl-material-compat.h
/usr/include/cogl/cogl/deprecated/cogl-shader.h
/usr/include/cogl/cogl/deprecated/cogl-texture-deprecated.h
/usr/include/cogl/cogl/deprecated/cogl-type-casts.h
/usr/include/cogl/cogl/deprecated/cogl-vertex-buffer.h
/usr/include/cogl/cogl/gl-prototypes/cogl-core-functions.h
/usr/include/cogl/cogl/gl-prototypes/cogl-gles2-functions.h
/usr/include/cogl/cogl/gl-prototypes/cogl-glsl-functions.h
/usr/include/cogl/cogl/gl-prototypes/cogl-in-gles-core-functions.h
/usr/include/cogl/cogl/gl-prototypes/cogl-in-gles2-core-functions.h
/usr/lib64/libcogl-gles2.so
/usr/lib64/libcogl-pango.so
/usr/lib64/libcogl-path.so
/usr/lib64/libcogl.so
/usr/lib64/pkgconfig/cogl-1.0.pc
/usr/lib64/pkgconfig/cogl-2.0-experimental.pc
/usr/lib64/pkgconfig/cogl-gl-1.0.pc
/usr/lib64/pkgconfig/cogl-gles2-1.0.pc
/usr/lib64/pkgconfig/cogl-gles2-2.0-experimental.pc
/usr/lib64/pkgconfig/cogl-pango-1.0.pc
/usr/lib64/pkgconfig/cogl-pango-2.0-experimental.pc
/usr/lib64/pkgconfig/cogl-path-1.0.pc
/usr/lib64/pkgconfig/cogl-path-2.0-experimental.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcogl-gles2.so.20
/usr/lib64/libcogl-gles2.so.20.4.2
/usr/lib64/libcogl-pango.so.20
/usr/lib64/libcogl-pango.so.20.4.2
/usr/lib64/libcogl-path.so.20
/usr/lib64/libcogl-path.so.20.4.2
/usr/lib64/libcogl.so.20
/usr/lib64/libcogl.so.20.4.2

%files locales -f cogl.lang
%defattr(-,root,root,-)

