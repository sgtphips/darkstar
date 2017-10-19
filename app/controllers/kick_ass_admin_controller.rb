class KickAssAdminController < ApplicationController
	layout "admin/base"

	def index
		@post = Post.filter_by('created_at').limit[:5]
	end


private
	def kickass_params
		params.require(:post).permit(:title, :author, :body)
	end
end
