class Post < ApplicationRecord
  belongs_to :user, counter_cache: true
  belongs_to :category, counter_cache: true
  has_many :comments
  has_and_belongs_to_many :tags
  
  validates :name, :content presence: true
end
