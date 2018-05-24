# Work


#for geometry
db.collection_name.createIndex( { location: "2dsphere" } )


db.collection.find({  
	location:{  
		$near :{  
			$geometry :{type:"Point", coordinates:[LNG, LAT]},  
			$minDistance:0,  
			$maxDistance:500  
		}  
	}  
})  
