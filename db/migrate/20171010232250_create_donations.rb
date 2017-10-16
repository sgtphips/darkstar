class CreateDonations < ActiveRecord::Migration[5.1]
  def change
    create_table :donations do |t|
      t.string :title
      t.string :bitcoin_wallet_address
      t.text :body

      t.timestamps
    end
  end
end
