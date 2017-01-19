using UnityEngine;
using System.Collections;

public class ChangeMat : MonoBehaviour {
	public Material mMaterial;
	// Use this for initialization
	void Start () 
	{
		Renderer lRender = GetComponent<Renderer> ();
		lRender.material = mMaterial;
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
