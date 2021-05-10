characters = ['a','b','c','d','e'] #,'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

function generator(length)
    password = ""
    for i in 1:length
        random = 
        password *= string(Base.rand(characters))
    end
    password
end

randompasswords = []
for i in 1:100
    push!(randompasswords, generator(8))
end

display(randompasswords)
