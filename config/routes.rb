Rails.application.routes.draw do
  resources :donations
  resources :updates
  resources :posts
  resources :videos
  resources :audios

  get "about" => "static#about"
  get "contact" => "static#contact"
  get "kickassadmin" => "kick_ass_admin#index"
  root "static#index"
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
