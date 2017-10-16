class KickAssAdminController < ApplicationController
	layout "admin/base"

	def index
		render "admin/index"
	end
end
