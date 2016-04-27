#!/bin/bash

DEVICE=
BITRATE=192

TMPPWD=$(pwd)
TMPDIR="$TMPPWD/tmp"
mkdir -p "$TMPDIR" 2>&1 > /dev/null
cd "$TMPDIR"

function printusage {
  echo "Usage:  $0 [OPTIONS]"
  echo "        OPTIONS:"
  echo "          -d <devicenode>      cdrom device to use"
  echo "          -b <bitrate>         changes the lame bitrate"
}

#function performs a cddb request to the
#inf file associated with the given track number
function cddb_query {
  TRACK=$1
  PROPERTY=$2
  
  if [ ${#TRACK} -le 1 ]; then
    TRACK="0$TRACK"
  fi
  
  trackfile="tmp/audio_${TRACK}.inf"
  VALUE=$(awk "/^$PROPERTY/ {\$1=\"\"; print \$0; next;}" $trackfile)
  echo "$VALUE" | sed -e "s/^ //g" -e "s/'//g" -e "s/\//-/g"
  #eval "echo $VALUE"
}

while getopts d:b: o
do
  case "$o" in
    d)
      EDEVICE="$OPTARG"
      DEVICE="-D $EDEVICE"
      echo "using $DEVICE for cdda2wav"
      ;;
    b)
      BITRATE="$OPTARG"
      echo "using -b $BITRATE for lame"
      ;;
    *)
      printusage
      exit 1
      ;;
  esac
done

cdda2wav -L 0 -B -g $DEVICE
eject $EDEVICE

cd "$TMPPWD"

if [ $? -ne 0 ]; then
  exit 1
fi

for I in $(find "tmp" -name "*.inf"); do
  TRACK="$(echo $I | grep -Eoe "[0-9][0-9]")"
  AFILE="${I%%.inf}.wav"
  
  Albumperformer="$(cddb_query $TRACK Albumperformer)"    
  Performer="$(cddb_query $TRACK Performer)"
  if [ "$Performer" != "" ]; then
    Performer="$Albumperformer"
  fi
  
  Albumtitle="$(cddb_query $TRACK Albumtitle)"
  Tracknumber="$(cddb_query $TRACK Tracknumber)"
  Tracktitle="$(cddb_query $TRACK Tracktitle)"

    
  MFILE="$TRACK ${Albumtitle} - ${Tracktitle}.mp3"
  ODIR="$TMPPWD/$Albumperformer - $Albumtitle"
  echo "Converting $AFILE to \"$MFILE\" using ID3: "
  echo -e "\tAlbum:  $Albumtitle"
  echo -e "\tArtist: $Performer"
  echo -e "\tTrack:  $Tracknumber"
  echo -e "\tTitle:  $Tracktitle"
  echo -e ""
  echo -e "to \"$ODIR\""
  echo -e ""
  
  mkdir -p "$ODIR"
  MFILE="$ODIR/$MFILE"
  
  lame -b "$BITRATE" "$AFILE" "$MFILE"
  id3tool -t "$Tracktitle" -a "$Albumtitle" -r "$Performer" -c "$Tracknumber" "$MFILE"
  
  echo "Remove .wav and cdda information"
  rm -v "$AFILE"
  rm -v "$I"
done

echo "Remove cddb index"
rm -v audio.cddb audio.cdindex
