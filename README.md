# Subs_organizer
This is a script to rename the srt files and place them inside the movie folder for every movie inside a movie collection.

It will only work if:
  1) each movie is stored inside a separate folder inside the base path were the script is placed
  2) inside each movie folder there is a single-file movie and no other files
  3) inside each movie folder there is a folder called "subs" with a srt file inside.

It will copy the srt file to the movie folder, rename it as the movie file name plus ".en.srt" and finaly rename the "subs" folder to "subs_processed"
