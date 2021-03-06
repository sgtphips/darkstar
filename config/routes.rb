Rails.application.routes.draw do
  devise_for :users
  resources :donations
  resources :updates
  resources :posts
  resources :videos
  resources :audios

  get "about" => "static#about"
  get "contact" => "static#contact"
  root "static#index"
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
