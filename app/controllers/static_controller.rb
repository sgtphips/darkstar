class StaticController < ApplicationController
	
	def index
		@posts = Post.all.limit(1).order('created_at DESC')
		@audios = Audio.all.limit(5).order('created_at DESC')
		@donations = Donation.all
		@videos = Video.all.limit(2).order('created_at DESC')
		@updates = Update.all
	end
	def about
		
	end
	def contact
		
	end
end
