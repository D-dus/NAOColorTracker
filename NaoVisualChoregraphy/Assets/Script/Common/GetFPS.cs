using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class GetFPS : MonoBehaviour {
	float deltaTime;
	Text fps;
	// Use this for initialization
	void Start () {
		deltaTime = 0;
		fps = gameObject.GetComponent<Text> ();
	}
	
	// Update is called once per frame
	void Update () 
	{
		deltaTime += (Time.deltaTime - deltaTime) * 0.1f;
		fps.text = "FPS : " + 1f / Time.deltaTime;
	}
}
