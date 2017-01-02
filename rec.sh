ffmpeg -f oss -acodec pcm_s16le -ac 1 -ar 16000 -vol 4096 -vn -i /dev/dsp /tmp/rec2.wav

ffmpeg -i /tmp/rec.wav  /tmp/output.flac
