require "csv"

prices = CSV.read("allabove.csv", { :col_sep => "\t" }) 


for i in prices
   j=i  #create a variable to go looking for the destination now as a start later
   start = i[0]
   dest = i[1]
   price = i[2]
   #puts "start #{start} end #{dest} price #{price}"
   #find when this start is the destination and this destination is the start
   for j in prices
   		start2 = j[0]
   		dest2 = j[1]
   		price2 = j[2]
   		if  dest == start2
   			if start == dest2
   				difference = price2.to_i - price.to_i
   				puts "#{start2}	#{dest2}	#{difference}"
   			end

   		end
   end
end
