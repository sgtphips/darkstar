json.extract! video, :id, :title, :link_to_video, :description, :created_at, :updated_at
json.url video_url(video, format: :json)
