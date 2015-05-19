require "csv"

#prices = CSV.read("out2.csv", { :col_sep => "\t" }) 
prices = CSV.read("allabove.csv", { :col_sep => "\t" }) 
  #puts row.inspect

#prices.each{ |row| puts row[0]}

for i in prices
   #puts "Value of local variable is #{i}"
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
   				difference = price.to_i - price2.to_i 
   				difference2 = price.to_i.fdiv(price2.to_i).round(1)
   				puts "#{start}	#{dest}	#{difference}	#{difference2}"
   			end

   		end
   end
end


