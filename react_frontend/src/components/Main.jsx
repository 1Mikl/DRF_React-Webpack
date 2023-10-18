import React, {useState, useEffect} from 'react';
import axios from "axios";

function Main() {
    const [isLoading, setLoading] = useState(true);
    const [categories, setCategories] = useState();

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/categories/").then(res => {
            setCategories(res.data);
            setLoading(false);
        });
    }, []);

    if (isLoading) {
        return <h1>Loading...</h1>;
    }
    return (
        <>
            <h1>Рецепты:</h1>
            <div className="buttons">
                {categories.map((name) => (
                    <a key={name.categoryType} className="category" href={`/category/${name.categoryType}`}>{name.categoryType}</a>
                ))}
            </div>
        </>
    );
}


export default Main

