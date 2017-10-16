class CreateAudios < ActiveRecord::Migration[5.1]
  def change
    create_table :audios do |t|
      t.string :title
      t.string :audio
      t.datetime :created_at
      t.datetime :updated_at

      t.timestamps
    end
  end
end
