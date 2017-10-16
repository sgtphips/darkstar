class CreateUpdates < ActiveRecord::Migration[5.1]
  def change
    create_table :updates do |t|
      t.string :title
      t.string :author
      t.text :body

      t.timestamps
    end
  end
end
