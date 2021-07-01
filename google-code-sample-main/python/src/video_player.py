"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""
    #instantiate 
    def __init__(self):
        self._video_library = VideoLibrary()
        self.play=False
        self.new_play=None
        self.current_play=None
        self.isPause=False


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos()) #get number of video
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        displayList=[] 
        for id,video in self._video_library.get_all_video_info().items(): 
            #Tags construction
            hashtag= "" #[tag for tag in videos.tags]
            hashtag+="["
            for i in video.tags:
                hashtag+=i+" "
            hashtag=hashtag.strip()
            hashtag+="]"

            displayList.append([video.title,f"({id})",hashtag]) # append the array in the right format
        displayList.sort() #sort Array
  
        print("Here's a list of all available videos:")
        for item in displayList:
            print(*item, sep=' ') #print list of all videos




    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
 
       """
       # get video to play
        self.new_play=self._video_library.get_video(video_id)

        if self.new_play == None: # if it does not exist
            print("Cannot play video: Video does not exist")
            #self.play=False
            #self.current_play=None
            

        else: #if exist
            
            if self.play==False: #if nothing is playing
                print("Playing video:",self.new_play.title)
                self.play=True
                self.current_play=self.new_play.title

            else: # If video is playing, stop it and play the new one
                
                print("Stopping video:",self.current_play)
                self.new_play=self._video_library.get_video(video_id)
                print("Playing video:",self.new_play.title)
                self.current_play=self.new_play.title
            self.isPause=False

#        if self.play==False: 
#            self.play_vid=self._video_library.get_video(video_id)
#            if self.play_vid == None:
 #               print("Cannot play video: Video does not exist")
 #               self.play=False
  #          else:
  #              print("Playing video:",self.play_vid.title)
  #              self.play=True
               

  #      else:
   #         if self.play_vid==None:          
    #            self.play=True
     #           print("Cannot play video: Video does not exist")
     #           self.play=False
      #      else:
       #         print(self.play_vid)
        #        self.stop_video(self.play_vid.title)
         #       self.play_vid=self._video_library.get_video(video_id)
          #      print("Playing video:",self.play_vid.title)
            


    def stop_video(self):
     #   title=self.current_play
     #   if self.isStop==False:

    #        """Stops the current video."""
    #        print("Stopping video: {}".format(title))
     #       #print("stop_video needs implementation")
    #        self.isStop=True
    #        self.play_vid=None
    #    else:
    #        print("Cannot stop video: No video is currently playing")


        # if no video playing
        if self.current_play==None:
            print("Cannot stop video: No video is currently playing")
        else:
            #else stop video
            print("Stopping video:",self.current_play)
        #reset variable
        self.new_play=None
        self.current_play=None
        self.play=False
        self.isPause=None

    

    def play_random_video(self):
        """Plays a random video from the video library."""
        self.new_play=random.choice(list(self._video_library.get_all_video_info().values()))# get all video info
        if self.current_play==None: # if nothing is playing, play random one
            print("Playing video:",self.new_play.title)

        else: #else stop current video and play new random one
            print("Stopping video:",self.current_play)
            print("Playing video:",self.new_play.title)
        self.current_play=self.new_play.title
        self.play=True

    def pause_video(self):
        """Pauses the current video."""

        if self.current_play==None: # if no video is playing, no pause available
            print("Cannot pause video: No video is currently playing")
            self.play=False
        else: # else if video already pause, cannot pause again
            if self.isPause==False:
                print("Pausing video:",self.current_play)
                self.isPause=True
            elif self.isPause==True: # if video playing, pause video
                print("Video already paused:",self.current_play)
            self.play=True
        

    def continue_video(self):
        """Resumes playing the current video."""
        if self.current_play==None: #if no video playing, cannot resume video
            print("Cannot continue video: No video is currently playing")
            self.play=False
        else: # else if video was pause, resume video. if video not pause, no need to resume it
            if self.isPause==False: 
                print("Cannot continue video: Video is not paused")

            else: 
                print("Continuing video: Amazing Cats")
            self.isPause=False
            self.play=True
        
        

    def show_playing(self):
        """Displays video currently playing."""
    
        #[video.title,f"({id})",[tag for tag in video.tags]]
        if self.current_play == None : # if nothing is playing
            print("No video is currently playing")
        else: #else retrieve all videos
            for id,videos in self._video_library.get_all_video_info().items():
                if self.current_play == videos.title: # compare playing video to all videos
                    
                    hashtag= "" #[tag for tag in videos.tags]
                    hashtag+="["
                    for i in videos.tags:
                        hashtag+=i+" "
                    hashtag=hashtag.strip()
                    hashtag+="]" #construct the structure to display
                    if self.isPause==False:
                        #print("TEST:",videos.tags)
                        print("Currently playing:",videos.title,f"({id})",hashtag)#,str([tag for tag in videos.tags]).replace(',',' '))
                    elif self.isPause==True: 
                        print("Currently playing:",videos.title,f"({id})",hashtag,"- PAUSED")#str([tag for tag in videos.tags]).replace(',',' '),"- PAUSED")




    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
