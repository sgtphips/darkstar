json.extract! donation, :id, :title, :bitcoin_wallet_address, :body, :created_at, :updated_at
json.url donation_url(donation, format: :json)
