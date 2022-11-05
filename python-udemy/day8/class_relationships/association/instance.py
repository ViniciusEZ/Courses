from day8.class_relationships.association.association import *

writer = Writer('Vinicius')
pen = Pen('BIC')
typewriter = TypeWriter()
writer.tool = typewriter
writer.tool.writing()
