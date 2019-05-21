#!/bin/bash

##cvlc v4l2:// :v4l2-vdev="/dev/video0" --sout '#transcode{vcodec=x264{keyint=60,idrint=2},vb=400,width=368,heigh=208,acodec=mp4a,ab=32,channels=2,fps=25}:duplicate{dst=std{access=http{mime=video/x-ms-wmv},mux=asf,dst=:8082/}}' --no-sout-audio
cvlc v4l2:// :v4l2-vdev="/dev/video0" --sout '#transcode{vcodec=x264{keyint=60,idrint=2},vb=400,width=368,heigh=208,acodec=mp4a,ab=32,channels=2,fps=25}:duplicate{dst=std{access=http{mime=video/x-ms-wmv},mux=ffmpeg{mux=flv},dst=:8082/}}' --no-sout-audio
#cvlc v4l2:// :v4l2-vdev="/dev/video0" --sout '#transcode{vcodec=x264{keyint=60,idrint=2},vb=400,width=1024,height=576,acodec=mp4a,ab=32,channels=2,fps=15}:duplicate{dst=std{access=http{mime=video/x-ms-wmv},mux=ffmpeg{mux=flv},dst=:8082/}}' --no-sout-audio
