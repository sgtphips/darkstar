class StaticController < ApplicationController
	def index
		@posts = Post.all
		@audios = Audio.all
		@donations = Donation.all
		@videos = Video.all
		@updates = Update.all
	end
	def about
		
	end
	def contact
		
	end
end
